# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_16_5_coroutil
   Description :   预激协程的装饰器
   date：          2022/3/8
-------------------------------------------------
"""
from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    """装饰器： 向前执行到第一个`yield`表达式，预激`func`"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()
    print(getgeneratorstate(coro_avg))
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
