# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.22
   Description :
   date：          2022/2/12
-------------------------------------------------
"""

from functools import reduce
from operator import mul


# def fact(n):
#     return reduce(lambda a, b: a * b, range(1, n + 1))

def fact(n):
    return reduce(mul, range(1, 11))
