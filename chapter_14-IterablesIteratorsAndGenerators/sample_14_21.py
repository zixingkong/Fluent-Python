# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_21
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

list(itertools.groupby('LLLLAAGGG'))  # ➊
# [('L', <itertools._grouper object at 0x102227cc0>),
# ('A', <itertools._grouper object at 0x102227b38>),
# ('G', <itertools._grouper object at 0x102227b70>)]
for char, group in itertools.groupby('LLLLAAAGG'):  # ➋
    print(char, '->', list(group))
# L -> ['L', 'L', 'L', 'L']
# A -> ['A', 'A',]
# G -> ['G', 'G', 'G']
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)  # ➌
animals
# ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark',
# 'giraffe', 'dolphin']
for length, group in itertools.groupby(animals, len):  # ➍
    print(length, '->', list(group))

# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']
for length, group in itertools.groupby(reversed(animals), len):  # ➎
    print(length, '->', list(group))
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']
