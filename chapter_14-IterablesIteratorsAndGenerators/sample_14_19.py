# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_19
   Description :
   date：          2022/2/22
-------------------------------------------------
"""
import itertools

ct = itertools.count()  # ➊
next(ct)  # ➋
# 0
next(ct), next(ct), next(ct)  # ➌
# (1, 2, 3)
list(itertools.islice(itertools.count(1, .3), 3))  # ➍
# [1, 1.3, 1.6]
cy = itertools.cycle('ABC')  # ➎
next(cy)
# 'A'
list(itertools.islice(cy, 7))  # ➏
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']
rp = itertools.repeat(7)  # ➐
next(rp), next(rp)
# (7, 7)
list(itertools.repeat(8, 4))  # ➑
# [8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5)))  # ➒
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
