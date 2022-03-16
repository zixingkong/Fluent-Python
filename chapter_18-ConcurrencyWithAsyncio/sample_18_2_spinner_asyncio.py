# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_18_2_spinner_asyncio.py
   Description :
   date：          2022/3/16
-------------------------------------------------
"""
import asyncio
import itertools
import sys


@asyncio.coroutine  # ➊
def spin(msg):  # ➋
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # ➌
        except asyncio.CancelledError:  # ➍
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # ➎
    # 假装等待I/O一段时间
    yield from asyncio.sleep(3)  # ➏
    return 42


@asyncio.coroutine
def supervisor(): # ➐
    spinner = asyncio.async(spin("thinking!"))  # ➑
    print('spinner object:', spinner)  # ➒
    result = yield from slow_function()  # ➓
    spinner.cancel()  # 11
    return result


def main():
    loop = asyncio.get_event_loop()  # 12
    result = loop.run_until_complete(supervisor())  # 13
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
