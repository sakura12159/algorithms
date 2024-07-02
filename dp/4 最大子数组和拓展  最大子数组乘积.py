# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 15:05
@Author  : zxy
@File    : 4 最大子数组和拓展  最大子数组乘积.py
"""
from mods import *

"""
https://leetcode.cn/problems/maximum-product-subarray/
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），
并返回该子数组所对应的乘积。
"""


def func(nums: List[int]) -> int:
    mx, pre_max, pre_min = -inf, 1, 1  # 记录最大前缀乘积和最小前缀乘积
    for i in nums:
        if i < 0:  # 如果当前元素为负，交换最大最小前缀乘积
            pre_max, pre_min = pre_min, pre_max
        pre_max, pre_min = max(pre_max * i, i), min(pre_min * i, i)
        mx = max(mx, pre_max)
    return mx


if __name__ == '__main__':
    nums = [2, 3, -2, 4, -5, -4]
    print(func(nums))
