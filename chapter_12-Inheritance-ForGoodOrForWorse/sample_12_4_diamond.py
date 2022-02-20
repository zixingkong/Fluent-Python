# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_12_4_diamond
   Description :
   date：          2022/2/20
-------------------------------------------------
"""


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.pong()
    print(D.__mro__)
    d.ping()
    print('*' * 80)
    d.pingpong()
