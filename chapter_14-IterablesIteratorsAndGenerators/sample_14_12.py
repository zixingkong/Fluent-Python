# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_12
   Description :   生成器函数是制造生成器的工厂
   date：          2022/2/21
-------------------------------------------------
"""


def aritprog_gen(begin,step,end=None):
    result = type(begin+step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index
