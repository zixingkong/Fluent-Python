# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.23
   Description :
   date：          2022/2/14
-------------------------------------------------
"""

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


if __name__ == '__main__':
    print(registry)
    print('-' * 80)
    print(register()(f3))
    print('-' * 80)
    print(registry)
    print('-' * 80)
    print(register(active=False)(f2))
    print('-' * 80)
    print(registry)
