# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_2.1
   Description :
   date：          2022/2/8
-------------------------------------------------
"""

"""
序列的分类
1.按照存放的是对象的引用还是值
    容器序列：list
            tuple 
            collections.deque 
            
    扁平序列：
            str 
            bytes
            bytearray
            memoryview
            array.array
2.按照能否被修改
    可变序列(MutableSequence)：
            list 
            bytearray
            array.array
            collections.deque 
            memoryview
    不可变序列(Sequence)：
            tuple
            str 
            bytes
"""

# 列表推导式
symbols = '$¢£¥€¤'
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))

# codes = [ord(symbol) for symbol in symbols]
# print(codes)

# beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
# print(beyond_ascii)

# beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
# print(beyond_ascii)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
for color in colors:
    for size in sizes:
        print((color, size))
# tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)
