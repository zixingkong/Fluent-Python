# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     example
   Description :
   date：          2022/3/16
-------------------------------------------------
"""

import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


coro = main()

asyncio.run(coro)
