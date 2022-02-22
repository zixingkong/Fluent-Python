# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     yield_from
   Description :   yield from 的第一个作用：代替循环
   date：          2022/2/22
-------------------------------------------------
"""


# def chain(*iterables):
#     for it in iterables:
#         for i in it:
#             yield i


def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
