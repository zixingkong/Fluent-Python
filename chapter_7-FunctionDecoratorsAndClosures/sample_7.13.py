# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.13
   Description :
   date：          2022/2/14
-------------------------------------------------
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
