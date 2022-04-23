from transmitter import Transmitter
from utils.async_input import async_input


class Messenger:
    @staticmethod
    async def text(ws_connect):
        async for websocket in ws_connect:
            message = await async_input("> ")
            await Transmitter.send(message, websocket)

    @staticmethod
    async def receive(ws_connect):
        async with ws_connect as websocket:
            await Transmitter.recieve(websocket)
