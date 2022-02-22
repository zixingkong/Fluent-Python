# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_18
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

list(itertools.product('ABC', range(2)))  # ➊
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
suits = 'spades hearts diamonds clubs'.split()
list(itertools.product('AK', suits))  # ➋
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
# ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
list(itertools.product('ABC'))  # ➌
# [('A',), ('B',), ('C',)]
list(itertools.product('ABC', repeat=2))  # ➍
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
list(itertools.product(range(2), repeat=3))
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
# (1, 0, 1), (1, 1, 0), (1, 1, 1)]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)

# ('A', 0, 'A', 0)
# ('A', 0, 'A', 1)
# ('A', 0, 'B', 0)
# ('A', 0, 'B', 1)
# ('A', 1, 'A', 0)
# ('A', 1, 'A', 1)
# ('A', 1, 'B', 0)
# ('A', 1, 'B', 1)
# ('B', 0, 'A', 0)
# ('B', 0, 'A', 1)
# ('B', 0, 'B', 0)
# ('B', 0, 'B', 1)
# ('B', 1, 'A', 0)
# ('B', 1, 'A', 1)
# ('B', 1, 'B', 0)
# ('B', 1, 'B', 1)
