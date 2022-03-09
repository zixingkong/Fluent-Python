# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2022/3/9 22:06
# @Author  : ty
# @File    : sample_16_18.py
# @Description: 
-------------------------------------------------
"""

""""
Result = yield from EXEP
"""

'''
i = iter(EXPR) ➊
try:
    _y = next(_i) ➋
except StopIteration as _e:
    _r = _e.value ➌
else:
    while 1: ➍
        _s = yield _y ➎
        try:
            _y = _i.send(_s) ➏
        except StopIteration as _e: ➐
            _r = _e.value
            break
RESULT = _r ➑
'''
