# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_8.16
   Description :
   date：          2022/2/15
-------------------------------------------------
"""

import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


if __name__ == '__main__':
    ender = weakref.finalize(s1, bye)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)
