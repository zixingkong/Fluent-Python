# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_11.8
   Description :
   date：          2022/2/18
-------------------------------------------------
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):  # ➊
        self._cards[position] = value

    def __delitem__(self, position):  # ➋
        del self._cards[position]

    def insert(self, position, value):  # ➌
        self._cards.insert(position, value)
