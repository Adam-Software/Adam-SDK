import os
import sys

import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from signal import SIGINT, SIGTERM
import logging
import argparse

adamVersion = "adam-2.7"

logger = logging.getLogger('Gamepad-Debug-Server')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_str)
ch.setFormatter(formatter)
logger.addHandler(ch)

async def off_board(websocket):
    logger.info('off-board client connected')

    while True:
        try:
            message = await websocket.recv()
            json_commands = json.loads(message)
            commands = []

            for element in json_commands['motors']:
                logger.info(f'{element}')

        except websockets.ConnectionClosed:
            logger.info('off-board client normal closed')
            break
        except Exception as err:
            logger.error(f'off-board client error: {err}')
            break

async def movement(websocket):
    logger.info('movement client connected')
    while True:
        try:
            message = await websocket.recv()
            json_commands = json.loads(message)
            x = json_commands['move']['x']
            y = json_commands['move']['y']
            z = json_commands['move']['z']

            logger.info(f'X: {x} Y: {y} Z: {z}')

        except websockets.ConnectionClosed:
            logger.info('movement client normal closed')
            break
        except Exception as err:
            logger.error(f'movement client error: {err}')
            break

routes = (
    route("/"),
    route(f"/{adamVersion}", subroutes=(
        route("/off-board", off_board, name="off-board"),
        route("/movement", movement, name="movement")
    )))

async def main():
    try:
        async with websockets.serve(router(routes), "0.0.0.0", 9001):
            await asyncio.Future()
    except asyncio.exceptions.CancelledError:
        logger.info('Server normally close')
    except Exception as err:
        logger.error(f'Server close with exception: {err}')

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())

    for signal in [SIGINT, SIGTERM]:
        loop.add_signal_handler(signal, main_task.cancel)
        loop.run_until_complete(main_task)
