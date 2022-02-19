# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_11.1
   Description :
   date：          2022/2/18
-------------------------------------------------
"""


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))
