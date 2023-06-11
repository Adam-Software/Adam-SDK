import os, sys

import asyncio
import json

import websockets
from yrouter import route
from yrouter_websockets import router

from signal import SIGINT, SIGTERM
import logging
import argparse

adamVersion = "adam-2.7"

logger = logging.getLogger('Debug-Socket-Server')
logger.setLevel(logging.INFO)
formatstr = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(formatstr)


async def offBoard(websocket):
    logger.info(f'offBoard client connected')

async def movement(websocket):
    logger.info(f'movement client connected')

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
    parser = argparse.ArgumentParser(description="Debug-Socket-Server")
    parser.add_argument('-l', '--log-file', default='debug-socket-server.log', help='Log files path')

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
        logger.info('Server close')
        loop.close()
