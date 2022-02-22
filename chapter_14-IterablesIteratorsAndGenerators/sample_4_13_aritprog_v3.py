# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_4_13_aritprog_v3
   Description :
   date：          2022/2/21
-------------------------------------------------
"""

import itertools


def aritpro_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen
