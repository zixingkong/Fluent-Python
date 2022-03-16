# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_18_1_spinner_thread
   Description :
   date：          2022/3/16
-------------------------------------------------
"""
import threading
import itertools
import time
import sys


class Signal:  # ➊
    go = True


def spin(msg, signal):  # ➋
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # ➌
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # ➍
        time.sleep(.1)
        if not signal.go:  # ➎
            break
    write(' ' * len(status) + '\x08' * len(status))  # ➏


def slow_function():  # ➐
    # 假装等待I/O一段时间
    time.sleep(3)  # ➑
    return 42


def supervisor():  # ➒
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner object:', spinner)  # ➓
    spinner.start() #11
    result = slow_function() #12
    signal.go = False #13
    spinner.join() #14
    return result


def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
