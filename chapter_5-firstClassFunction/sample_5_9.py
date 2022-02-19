# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.9
   Description :
   date：          2022/2/12
-------------------------------------------------
"""


class C:
    pass


def func():
    pass


if __name__ == '__main__':
    obj = C()
    chaji = sorted(set(dir(func)) - set(dir(obj)))
    print(chaji)
