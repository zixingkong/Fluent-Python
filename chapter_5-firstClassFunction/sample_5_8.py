# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.5
   Description :
   date：          2022/2/12
-------------------------------------------------
"""

import random

import self as self


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
