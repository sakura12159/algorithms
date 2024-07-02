# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 下午2:58
@Author  : zxy
@File    : 8 计数排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/counting-sort.html
计数排序，适用于小范围整数
    1 找出待排序的数组中最大和最小的元素
    2 统计数组中每个值为i的元素出现的次数，存入数组C的第i项
    3 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
    4 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
"""


def counting_sort(arr: List[int]) -> None:
    cnt = [0] * (max(arr) + 1)
    for x in arr:
        cnt[x] += 1

    p = 0
    for i, x in enumerate(cnt):
        if x:
            for j in range(p, p + x):
                arr[j] = i
            p += x


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    counting_sort(arr)
    print(arr)
