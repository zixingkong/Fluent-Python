# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_16-2
   Description :   协程产出多个值
   date：          2022/3/8
-------------------------------------------------
"""


def simple_coro2(a):
    print('-> Started: a = ', a)
    b = yield a
    print('-> Received: b = ', b)
    c = yield a + b
    print('-> Received: c = ', c)


if __name__ == '__main__':
    my_coro2 = simple_coro2(14)
    from inspect import getgeneratorstate

    print(getgeneratorstate(my_coro2))
    next(my_coro2)
    getgeneratorstate(my_coro2)
    my_coro2.send(28)
    my_coro2.send(99)
    getgeneratorstate(my_coro2)
