import os
import sys

import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from signal import SIGINT, SIGTERM
import logging

logger = logging.getLogger('Debug-Socket-Server')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

adamVersion = "adam-2.7"


async def off_board(websocket):
    logger.info('off-board client connected')

    try:
        async for message in websocket:
            json_commands = json.loads(message)
            logger.info(json_commands)
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

            logger.info(f'{linear_velocity} f{angular_velocity}')
    except websockets.ConnectionClosed:
        logger.info('movement client normal closed')
        linear_velocity = (0, 0)
        angular_velocity = 0
        logger.info(f'{linear_velocity} f{angular_velocity}')
    except Exception as err:
        logger.info(f'movement client error: {err}')
        linear_velocity = (0, 0)
        angular_velocity = 0
        logger.info(f'{linear_velocity} f{angular_velocity}')


async def debug(websocket):
    logger.info('debug client connect')
    try:
        async for message in websocket:
            logger.info(message)
    except websockets.ConnectionClosed:
        logger.info('debug client normal closed')
    except Exception as err:
        logger.warning(f'Debug client exception: {err}')

routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        route("/off-board", off_board, name="off-board"),
        route("/movement", movement, name="movement"),
        route("/debug", debug, name="debug")
    )))


async def main():
    logger.debug("server start")
    async with websockets.serve(router(routes), "0.0.0.0", 9001):
        await asyncio.Future()


if __name__ == "__main__":
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
        logger.info('Server close')
        loop.close()
