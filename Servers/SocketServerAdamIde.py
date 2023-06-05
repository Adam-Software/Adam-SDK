import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from AdamManager import AdamManager
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands
#from serial_motor_control.MotorControl import MotorControl
from signal import SIGINT, SIGTERM

adamVersion = "adam-2.6"
adamController = AdamManager()

async def offBoard(websocket):
    
    async for message in websocket:
        jsonCommands = json.loads(message)
        commands = []

        for element in jsonCommands['motors']:
            commands.append(MotorCommand(**element))

        adamController.handle_command(SerializableCommands(commands))

async def movement(websocket):
    
    async for message in websocket:
        try:
            jsonCommands = json.loads(message)
            x = jsonCommands['move']['x']
            y = jsonCommands['move']['y']
            z = jsonCommands['move']['z']
            
            linear_velocity = (x, y)
            angular_velocity = z
            adamController.move(linear_velocity, angular_velocity)
                
        except websockets.ConnectionClosedOK:
            print('Debug client disconnect')
            linear_velocity = (0, 0)
            angular_velocity = 0
            adamController.move(linear_velocity, angular_velocity)
        except:
            linear_velocity = (0, 0)
            angular_velocity = 0
            adamController.move(linear_velocity, angular_velocity)

async def debug(websocket):
    
        async for message in websocket:
            try:
                print(message)        
            except websockets.ConnectionClosedOK:
                print('Debug client disconnect')
            except:
                print('Debug client crash')

    

routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        route("/off-board", offBoard, name="off-board"),     
        route("/movement", movement, name="movement"),
        route("/debug", debug, name="debug")
    )))


async def main():
    try:
        async with websockets.serve(router(routes), "0.0.0.0", 8001):
            await asyncio.Future()  # run forever
    except:
        print('Server crash')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    for signal in [SIGINT, SIGTERM]:
        loop.add_signal_handler(signal, main_task.cancel)
    try:
        loop.run_until_complete(main_task)
    except:
        print('Server crash')
        loop.close()
    finally:
        print('Server stopped')
        loop.close()
