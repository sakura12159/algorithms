# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 上午10:44
@Author  : zxy
@File    : 5 归并排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/merge-sort.html
归并排序
    1 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
    2 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
    3 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
    4 重复步骤 3 直到某一指针达到序列尾；
    5 将另一序列剩下的所有元素直接复制到合并序列尾。
"""


# 递归
def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n < 2:
        return arr

    return merge(merge_sort(arr[:n // 2]), merge_sort(arr[n // 2:]))


def merge(left: List[int], right: List[int]):
    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + left if left else res + right


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    arr = merge_sort(arr)
    print(arr)
