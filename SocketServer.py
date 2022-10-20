import asyncio
import json

import websockets

from AdamController import AdamController
from Models.MotorCommand import MotorCommand
from Models.SerializableCommands import SerializableCommands


async def adam(websocket):
    adamController = AdamController()

    async for message in websocket:
        jsonCommands = json.loads(message)
        commands = []

        for element in jsonCommands['motors']:
            commands.append(MotorCommand(**element))

        adamController.HandleCommand(SerializableCommands(commands))


async def main():
    async with websockets.serve(adam, "0.0.0.0", 8000):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
