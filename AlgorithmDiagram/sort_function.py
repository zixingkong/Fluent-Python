# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sort_function
   Description :
   date：          2022/2/3
-------------------------------------------------
"""
import pysnooper


# 排序算法
# 1.选择排序：O(n**2)

def find_smallest(arr):
    smallest_index = 0
    smallest = arr[0]
    for index, item in enumerate(arr):
        if smallest >= item:
            smallest_index = index
            smallest = item

    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


# 2.快速排序: 分而治之的思想,时间复杂度O(nlogn)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        base = arr[0]
        less = [i for i in arr[1:] if i <= base]
        great = [i for i in arr[1:] if i > base]
        return quick_sort(less) + [base] + quick_sort(great)


if __name__ == '__main__':
    arr = [2, 4, 1, 3, 5, 9, 7, 6, 8]
    # print(selection_sort(arr))
    print(quick_sort(arr))
