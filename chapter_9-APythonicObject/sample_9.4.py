# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_9.4
   Description :
   date：          2022/2/16
-------------------------------------------------
"""


class Demo:
    @classmethod
    def kclassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == '__main__':
    print(Demo.kclassmeth())
    print(Demo.kclassmeth('spam'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))
