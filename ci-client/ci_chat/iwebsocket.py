import websockets
from transmitter import Transmitter


class IWebSocket:
    socket = websockets

    @staticmethod
    async def listen(port: int, hostname="localhost"):
        return IWebSocket.socket.connect(f"ws://{hostname}:{port}")
