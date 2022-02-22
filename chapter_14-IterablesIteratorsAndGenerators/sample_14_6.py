# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_6
   Description :
   date：          2022/2/21
-------------------------------------------------
"""


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


if __name__ == '__main__':
    for c in gen_AB():
        print('-->',c)
