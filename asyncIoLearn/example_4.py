# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     example_4
   Description :
   date：          2022/3/16
-------------------------------------------------
"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    res1 = await task1
    res2 = await task2

    print(res1)
    print(res2)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
