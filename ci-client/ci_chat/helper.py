import asyncio


async def upper_case(name: str):
    return name.upper()


async def func():
    string = "hello"
    return await upper_case(string)


result = asyncio.run(func())

print(result)
