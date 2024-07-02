# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 下午1:22
@Author  : zxy
@File    : 6 快速排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/quick-sort-2.html
快排
    1 从数列中挑出一个元素，称为 "基准"（pivot）;
    2 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
    在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
    3 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；
"""


def quick_sort(arr: List[int], left: int, right: int) -> None:
    def partition() -> int:
        def swap(i: int, j: int) -> None:
            arr[i], arr[j] = arr[j], arr[i]

        res = left + 1
        pivot = arr[left]
        for i in range(left + 1, right + 1):
            if arr[i] < pivot:
                swap(i, res)  # 将小于被挑选元素的元素按序放到被挑选元素后面
                res += 1  # 分割点右移
        swap(left, res - 1)  # 将挑选的元素置于分割点，此时该元素左侧元素都小于该元素
        return res - 1

    if left < right:
        partition_idx = partition()
        quick_sort(arr, left, partition_idx - 1)
        quick_sort(arr, partition_idx + 1, right)


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
