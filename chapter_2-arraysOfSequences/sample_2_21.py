# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.21
   Description :
   date：          2022/2/9
-------------------------------------------------
"""
import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
