# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 14:57
@Author  : zxy
@File    : 3 最大子数组和.py
"""
from mods import *

"""
https://leetcode.cn/problems/maximum-subarray/
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""


def func(nums: List[int]) -> int:
    # dfs(i) = max(dfs(i - 1), 0) + nums[i]

    # Kadane算法
    # pre, mx = 0, -inf
    # for i in range(len(nums)):
    #     pre = max(pre, 0) + nums[i]
    #     mx = max(mx, pre)
    # return mx

    # 前缀和
    mx, min_pre_sum, pre_sum = -inf, 0, 0  # 记录最小前缀和与当前前缀和
    for i in nums:
        pre_sum += i  # 计算当前前缀和
        mx = max(mx, pre_sum - min_pre_sum)  # 更新前缀和的最大值
        min_pre_sum = min(min_pre_sum, pre_sum)  # 更新前缀和的最小值
    return mx


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(func(nums))
