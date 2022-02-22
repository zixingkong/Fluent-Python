# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_11
   Description :
   date：          2022/2/21
-------------------------------------------------
"""


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


if __name__ == '__main__':
    ap = ArithmeticProgression(0, 1, 3)
    print(list(ap))
    ap = ArithmeticProgression(1, .5, 3)
    print(list(ap))
    ap = ArithmeticProgression(0, 1 / 3, 1)
    print(list(ap))
