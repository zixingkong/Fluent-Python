# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_17
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

list(itertools.chain('ABC', range(2)))  # ➊
# ['A', 'B', 'C', 0, 1]
list(itertools.chain(enumerate('ABC')))  # ➋
# [(0, 'A'), (1, 'B'), (2, 'C')]
list(itertools.chain.from_iterable(enumerate('ABC')))  # ➌
# [0, 'A', 1, 'B', 2, 'C']
list(zip('ABC', range(5)))  # ➍
# [('A', 0), ('B', 1), ('C', 2)]
list(zip('ABC', range(5), [10, 20, 30, 40]))  # ➎
# [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
list(itertools.zip_longest('ABC', range(5)))  # ➏
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
list(itertools.zip_longest('ABC', range(5), fillvalue='?'))  # ➐
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
