# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午8:28
@Author  : zxy
@File    : 2 一维差分 与车相交的点.py
"""
from mods import *

"""
https://leetcode.cn/problems/points-that-intersect-with-cars/
给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。
对于任意下标 i，nums[i] = [starti, endi] ，其中 starti 是第 i 辆车的起点，endi 是第 i 辆车的终点。
返回数轴上被车 任意部分 覆盖的整数点的数目。
"""


def func(nums: List[List[int]]) -> int:
    max_end = max(end for _, end in nums)
    diff = [0] * (max_end + 2)
    for start, end in nums:
        diff[start] += 1
        diff[end + 1] -= 1
    return sum(s > 0 for s in accumulate(diff))


if __name__ == '__main__':
    nums = [[3, 6], [1, 5], [4, 7]]
    print(func(nums))
