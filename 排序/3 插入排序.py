# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 上午10:15
@Author  : zxy
@File    : 3 插入排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/insertion-sort.html
插入排序
    1 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    2 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
"""


def insertion_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        pre_idx = i - 1
        cur = arr[i]
        while pre_idx >= 0 and arr[pre_idx] > cur:
            arr[pre_idx + 1] = arr[pre_idx]
            pre_idx -= 1
        arr[pre_idx + 1] = cur


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    insertion_sort(arr)
    print(arr)
