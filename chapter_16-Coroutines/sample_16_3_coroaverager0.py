# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_16_3_coroaverager0
   Description :   定义一个计算移动平均值得协程
   date：          2022/3/8
-------------------------------------------------
"""


def averager():
    totoal = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        totoal += term
        count += 1
        average = totoal / count


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(30))
    print(coro_avg.send(5))
