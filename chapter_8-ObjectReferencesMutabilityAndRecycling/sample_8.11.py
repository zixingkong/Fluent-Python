# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_8.11
   Description :
   date：          2022/2/15
-------------------------------------------------
"""


def f(a, b):
    a += b
    return a


if __name__ == '__main__':
    x = 1
    y = 2
    print(f(x, y))
    print(x, y)
    a = [1, 2]
    b = [3, 4]
    print(f(a, b))
    print(a, b)
    t = (10, 20)
    u = (30, 40)
    print(f(t, u))
    print(t, u)
