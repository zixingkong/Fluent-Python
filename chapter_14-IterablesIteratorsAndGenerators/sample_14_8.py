# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_8
   Description :
   date：          2022/2/21
-------------------------------------------------
"""


def gen_AB():  # ➊
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


res1 = [x * 3 for x in gen_AB()]  # ➋

for i in res1:  # ➌
    print('-->', i)
res2 = (x * 3 for x in gen_AB())  # ➍
print(res2)  # ➎

for i in res2:  # ➏
    print('-->', i)
