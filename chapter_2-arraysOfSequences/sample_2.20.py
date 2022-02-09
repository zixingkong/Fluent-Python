# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.20
   Description :
   date：          2022/2/9
-------------------------------------------------
"""
from docutils.writers.latex2e import fp

"""
列表 list
数组 array.array
队列 deque
        queue
        multiprocessing
        asyncio
        heapq 


"""

from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])
print(floats2 == floats)
