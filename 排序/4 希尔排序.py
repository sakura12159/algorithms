# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 上午10:23
@Author  : zxy
@File    : 4 希尔排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/shell-sort.html
https://zhuanlan.zhihu.com/p/122632213
希尔排序
    gap 取 1、5、19、41、109等
    1 先取一个小于 n 的整数 d1 作为第一个增量，把文件的全部记录分成 d1 个组。
    2 所有距离为 d1 的倍数的记录放在同一个组中，在各组内进行直接插入排序。
    3 取第二个增量 d2 小于 d1 重复上述的分组和排序，直至所取的增量 dt = 1 (dt小于dt - l小于…小于d2小于d1)，
    即所有记录放在同一组中进行直接插入排序为止。
"""


def shell_sort(arr: List[int], gap: int = 5) -> None:
    n = len(arr)
    while gap:
        for i in range(gap, n):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap //= 2


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    shell_sort(arr)
    print(arr)
