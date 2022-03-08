# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mirror
   Description :
   date：          2022/2/22
-------------------------------------------------
"""


class LookingGlass:
    def __enter__(self):  # ➊
        import sys
        self.original_write = sys.stdout.write  # ➋
        sys.stdout.write = self.reverse_write  # ➌
        return 'JABBERWOCKY'  # ➍

    def reverse_write(self, text):  # ➎
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # ➏
        import sys  # ➐
        sys.stdout.write = self.original_write  # ➑
        if exc_type is ZeroDivisionError:  # ➒
            print('Please DO NOT divide by zero!')
            return True  # ➓
