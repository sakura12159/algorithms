# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 上午10:07
@Author  : zxy
@File    : 2 选择排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/selection-sort.html
选择排序
    1 首先在未排序序列中找到最小元素，存放到排序序列的起始位置。
    2 再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
    3 重复第二步，直到所有元素均排序完毕。
"""


def selection_sort(arr: List[int]) -> None:
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    selection_sort(arr)
    print(arr)
