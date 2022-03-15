# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_17_6_demo_executor_map
   Description :
   date：          2022/3/15
-------------------------------------------------
"""
from time import sleep, strftime
from concurrent import futures


def display(*args):  # ➊
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):  # ➋
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t' * n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t' * n, n))
    return n * 10  # ➌


def main():
    display('Script starting.')
    executor = futures.ThreadPoolExecutor(max_workers=3)  # ➍
    results = executor.map(loiter, range(10))  # ➎
    display('results:', results)  # ➏
    display('Waiting for individual results:')
    for i, result in enumerate(results):  # ➐
        display('result {}: {}'.format(i, result))


main()
