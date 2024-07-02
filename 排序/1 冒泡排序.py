# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 上午9:57
@Author  : zxy
@File    : 1 冒泡排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/bubble-sort.html
冒泡排序
    1 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3 针对所有的元素重复以上的步骤，除了最后一个。
    4 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""


def bubble_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    bubble_sort(arr)
    print(arr)
