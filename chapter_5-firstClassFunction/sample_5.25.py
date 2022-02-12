# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.25
   Description :
   date：          2022/2/12
-------------------------------------------------
"""

from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))
