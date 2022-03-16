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

    ret = await asyncio.gather(task1,task2)

    print(ret)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
