from websockets import WebSocketClientProtocol
from message_logger import MessageLogger


class Transmitter:

    @staticmethod
    async def send(message, websocket: WebSocketClientProtocol) -> None:
        await websocket.send(message)
        await websocket.recv()

    @staticmethod
    async def recieve(websocket: WebSocketClientProtocol) -> None:
        async for message in websocket:
            MessageLogger.log(message)
