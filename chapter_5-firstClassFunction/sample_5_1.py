# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_5.1
   Description :
   date：          2022/2/12
-------------------------------------------------
"""


def factorial(n):
    '''
    return n!
    :param n:
    :return:
    '''
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(42))
    print(factorial.__doc__)
    print(type(factorial))

    fact = factorial
    print(fact)
    print(fact(5))
    print(list(map(factorial, range(11))))

    list_1 = [fact(n) for n in range(6)]
    print(list_1)
    list_2 = list(map(fact, filter(lambda n: n % 2, range(6))))
    print(list_2)
    list_3 = [fact(n) for n in range(6) if n % 2]
    print(list_3)

    print(dir(factorial))
