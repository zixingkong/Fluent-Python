# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.8
   Description :
   date：          2022/2/14
-------------------------------------------------
"""


class Average():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == '__main__':
    avg = Average()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)
