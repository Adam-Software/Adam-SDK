import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from adam_sdk import AdamManager
from adam_sdk import MotorCommand
from adam_sdk import SerializableCommands
from signal import SIGINT, SIGTERM
import logging
import argparse

adamVersion = "adam-2.6"
adamController = AdamManager()

logger = logging.getLogger('Socket-Server-Daemon')
logger.setLevel(logging.INFO)
formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(formatstr)


async def offBoard(websocket):
    logger.info(f'offBoard client connected')
    async for message in websocket:
        jsonCommands = json.loads(message)
        commands = []

        for element in jsonCommands['motors']:
            commands.append(MotorCommand(**element))

        adamController.handle_command(SerializableCommands(commands))


async def movement(websocket):
    logger.info(f'movement client connected')
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
            logger.info('movement client disconnect')
            linear_velocity = (0, 0)
            angular_velocity = 0
            adamController.move(linear_velocity, angular_velocity)
        except:
            linear_velocity = (0, 0)
            angular_velocity = 0
            adamController.move(linear_velocity, angular_velocity)


async def debug(websocket):
    logger.info(f'debug client connected')
    async for message in websocket:
        try:
            logger.info(message)
        except websockets.ConnectionClosedOK:
            logger.info('Debug client disconnect')
        except:
            logger.warning('Debug client crash')


routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        route("/off-board", offBoard, name="off-board"),
        route("/movement", movement, name="movement"),
        route("/debug", debug, name="debug")
    )))


async def main():
    try:
        async with websockets.serve(router(routes), "0.0.0.0", 8000):
            await asyncio.Future()  # run forever
    except:
        logger.warning('Server close with except')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notification daemon")
    parser.add_argument('-l', '--log-file', default='/var/log/socket-server.log', help='Log files path')

    args = parser.parse_args()
    fh = logging.FileHandler(args.log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    for signal in [SIGINT, SIGTERM]:
        loop.add_signal_handler(signal, main_task.cancel)
    try:
        loop.run_until_complete(main_task)
    except:
        loop.close()
    finally:
        logger.info('Server close with except')
        loop.close()
