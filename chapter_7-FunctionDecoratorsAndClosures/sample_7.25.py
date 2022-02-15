# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.25
   Description :
   date：          2022/2/14
-------------------------------------------------
"""
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # ➊
    def decorate(func):  # ➋
        def clocked(*_args):  # ➌
            t0 = time.time()
            _result = func(*_args)  # ➍
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)  # ➎
            result = repr(_result)  # ➏
            print(fmt.format(**locals()))  # ➐
            return _result  # ➑

        return clocked  # ➒

    return decorate  # ➓


if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)


    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)


    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)
