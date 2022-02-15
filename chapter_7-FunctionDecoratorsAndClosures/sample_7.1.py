# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.1
   Description :
   date：          2022/2/14
-------------------------------------------------
"""


def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


# target = deco(target)
if __name__ == '__main__':
    print(target())
    print(target)
