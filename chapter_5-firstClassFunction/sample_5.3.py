# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.3
   Description :
   date：          2022/2/12
-------------------------------------------------
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))
print(sorted(fruits, key=lambda word: word[::-1]))

judge_list = [callable(obj) for obj in (abs, str, 13)]
print(judge_list)
