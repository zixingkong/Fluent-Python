# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.5
   Description :
   date：          2022/2/9
-------------------------------------------------
"""

"""
生成器表达式
"""
symbols = '$¢£¥€¤'
test = tuple(ord(symbol) for symbol in symbols)
print(test)

import array

test2 = array.array('I', (ord(symbol) for symbol in symbols))
print(test2)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
