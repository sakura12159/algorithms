# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午3:51
@Author  : zxy
@File    : 1 查找边界 在排序数组中查找元素的第一个和最后一个位置.py
"""
from mods import *

"""
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
"""


def func(nums: List[int], target: int) -> List[int]:
    if not nums or target > nums[-1] or target < nums[0]:
        return [-1, -1]

    # 找左边界
    n = len(nums)
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    if nums[l] != target:
        return [-1, -1]

    tmp = l
    # 找右边界
    l, r = 0, n
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return [tmp, l - 1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(func(nums, target))
