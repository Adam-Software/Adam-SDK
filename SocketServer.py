import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from AdamController import AdamController
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands
from serial_motor_control.MotorControl import MotorControl
from signal import SIGINT, SIGTERM

adamVersion = "adam-2.6"


async def offBoard(websocket):
    adamController = AdamController()

    async for message in websocket:
        jsonCommands = json.loads(message)
        commands = []

        for element in jsonCommands['motors']:
            commands.append(MotorCommand(**element))

        adamController.HandleCommand(SerializableCommands(commands))


async def onboard(websocket):
    await websocket.send("onboard")


async def movement(websocket, motorId: int, speedFront: int, speedBack: int):
    motorControl = MotorControl()
    motorControl.MotionManage(motorId, speedFront, speedBack)
    await websocket.send("movement")


async def state(websocket):
    await websocket.send("state")

async def debug(websocket): 
    print('Debug client connected')
    while True:
        try:
            message = await websocket.recv()
            print(message)
        except websockets.ConnectionClosedOK:
            print('Debug client disconnect')
            break


routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        # compute vr on rasp board
        route("/onboard", onboard, name="onboard"),
        # compute vr on pc
        route("/off-board", offBoard, name="off-board"),
        # motor manage
        route("/movement/<int:motorId>/<int:speedFront>/<int:speedBack>", movement, name="movement"),
        route("/state", state, name="state"),
        route("/debug", debug, name="debug")
    )))


async def main():
    try:
        async with websockets.serve(router(routes), "0.0.0.0", 8000):
            await asyncio.Future()  # run forever
    except:
        pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    for signal in [SIGINT, SIGTERM]:
        loop.add_signal_handler(signal, main_task.cancel)
    try:
        loop.run_until_complete(main_task)
    finally:
        print('Server stopped')
        loop.close()
