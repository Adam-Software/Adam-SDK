import os
import sys

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

adamVersion = "adam-2.7"
adam_controller = AdamManager()

logger = logging.getLogger('Socket-Server-Daemon')
logger.setLevel(logging.ERROR)
format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_str)


async def off_board(websocket):
    logger.info(f'off-board client connected')

    try:
        async for message in websocket:
            json_commands = json.loads(message)
            commands = []

            for element in json_commands['motors']:
                commands.append(MotorCommand(**element))

            adam_controller.handle_command(SerializableCommands(commands))
    except websockets.ConnectionClosed:
        logger.info('off-board client normal closed')
    except Exception as err:
        logger.info(f'off-board client error: {err}')


async def movement(websocket):
    logger.info(f'movement client connected')
    try:
        async for message in websocket:
            json_commands = json.loads(message)
            x = json_commands['move']['x']
            y = json_commands['move']['y']
            z = json_commands['move']['z']

            linear_velocity = (x, y)
            angular_velocity = z
            adam_controller.move(linear_velocity, angular_velocity)

    except websockets.ConnectionClosed:
        logger.info('movement client normal closed')
        linear_velocity = (0, 0)
        angular_velocity = 0
        adam_controller.move(linear_velocity, angular_velocity)
    except Exception as err:
        logger.info(f'movement client error: {err}')
        linear_velocity = (0, 0)
        angular_velocity = 0
        adam_controller.move(linear_velocity, angular_velocity)


routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        route("/off-board", off_board, name="off-board"),
        route("/movement", movement, name="movement")
    )))


async def main():
    async with websockets.serve(router(routes), "0.0.0.0", 8000):
        await asyncio.Future()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket-Server-Daemon")
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
    except Exception as error:
        logger.error(f'Server loop close with except {error}')
        loop.close()
    finally:
        loop.close()
