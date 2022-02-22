# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_20
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

list(itertools.combinations('ABC', 2))  # ➊
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations_with_replacement('ABC', 2))  # ➋
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.permutations('ABC', 2))  # ➌
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
list(itertools.product('ABC', repeat=2))  # ➍
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'),
# ('C', 'A'), ('C', 'B'), ('C', 'C')]
