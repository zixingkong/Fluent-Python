# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.18
   Description :
   date：          2022/2/9
-------------------------------------------------
"""
import bisect
import random

import great as great

# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
#
# result = [grade(score) for score in [33, 99, 77, 89, 100]]
# print(result)

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)
