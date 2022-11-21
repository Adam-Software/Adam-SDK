import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from AdamController import AdamController
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands

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


async def movement(websocket):
    await websocket.send("movement")


async def state(websocket):
    await websocket.send("movement")


routes = (
    route(f"/off-board", offBoard, adamVersion),
    route(f"/onboard", onboard, adamVersion),
    route(f"/movement", movement, adamVersion),
    route(f"/state", offBoard, adamVersion),
)


async def main():
    async with websockets.serve(router(routes), "0.0.0.0", 8000):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
