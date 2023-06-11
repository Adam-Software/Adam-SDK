import os, sys

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

async def offBoard(websocket):
    logger.debug('offBoard client connected')

async def movement(websocket):
    logger.debug('movement client connected')

async def debug(websocket):
    logger.debug('debug client connected')

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
        logger.debug("server start")
        async with websockets.serve(router(routes), "0.0.0.0", 9001):
            await asyncio.Future()  # run forever
    except:
        logging.warning('server close with except')


if __name__ == "__main__":
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
