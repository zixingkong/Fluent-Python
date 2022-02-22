# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_22
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

list(itertools.tee('ABC'))
# [<itertools._tee object at 0x10222abc8>, <itertools._tee object at 0x10222ac08>]
g1, g2 = itertools.tee('ABC')
next(g1)
# 'A'
next(g2)
# 'A'
next(g2)
# 'B'
list(g1)
# ['B', 'C']
list(g2)
# ['C']
list(zip(*itertools.tee('ABC')))
# [('A', 'A'), ('B', 'B'), ('C', 'C')]
