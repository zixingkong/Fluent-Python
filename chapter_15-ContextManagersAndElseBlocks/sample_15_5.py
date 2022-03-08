# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_15_5
   Description :
   date：          2022/3/3
-------------------------------------------------
"""

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print(what)