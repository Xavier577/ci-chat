#!/usr/bin/env python

from ast import arg
import asyncio
from iwebsocket import IWebSocket
from messenger import Messenger


async def main():
    socket_connect = await IWebSocket.listen(port=8080)

    asyncio.create_task(Messenger.receive(socket_connect))
    asyncio.create_task(Messenger.text(socket_connect))

    # asyncio.gather(Messenger.receive(socket_connect),
    #                Messenger.text(socket_connect))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
