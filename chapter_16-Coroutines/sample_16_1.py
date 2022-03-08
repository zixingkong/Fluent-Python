# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_16
   Description :   协程的行为
   date：          2022/3/8
-------------------------------------------------
"""


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received: ', x)


if __name__ == '__main__':
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)
    my_coro.send(42)
