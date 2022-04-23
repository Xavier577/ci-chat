import asyncio
from concurrent.futures import ThreadPoolExecutor


async def async_input(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return (await asyncio.get_event_loop().run_in_executor(executor, input, prompt)).rstrip()
