# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午3:54
@Author  : zxy
@File    : 2 查找值 二分查找.py
"""
from mods import *

"""
https://leetcode.cn/problems/binary-search/
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
"""


def func(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(func(nums, target))
