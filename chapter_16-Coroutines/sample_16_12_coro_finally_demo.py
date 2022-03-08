# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_16_12_coro_finally_demo
   Description :
   date：          2022/3/8
-------------------------------------------------
"""


class DemoException(Exception):
    """为这次演示定义的异常类型"""


def demo_exc_handling():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))

        raise RuntimeException('This line should never run')
    finally:
        print('-> coroutine ending')


if __name__ == '__main__':
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    # exc_coro.send(22)
    # exc_coro.close()
    # exc_coro.throw(DemoException)
    exc_coro.throw(ZeroDivisionError)
    from inspect import getgeneratorstate

    getgeneratorstate(exc_coro)
