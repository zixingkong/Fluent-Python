# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_11_12.bingo
   Description :
   date：          2022/2/19
-------------------------------------------------
"""
import random

from sample_11_9_tombola import Tombola


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()
