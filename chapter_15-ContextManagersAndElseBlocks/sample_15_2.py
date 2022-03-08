# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_15_2
   Description :
   date：          2022/2/22
-------------------------------------------------
"""

from mirror import LookingGlass

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)
print('Back to normal.')
