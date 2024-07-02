# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 14:17
@Author  : zxy
@File    : 1 入门 打家劫舍.py
"""
from mods import *

"""
https://leetcode.cn/problems/house-robber/
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下，一夜之内能够偷窃到的最高金额。
"""


def func(nums: List[int]) -> int:
    # dfs(i) = max(dfs(i - 1), dfs(i - 2) + nums[i])

    # 记忆化搜索
    # @cache
    # def dfs(i):
    #     if i < 0:
    #         return 0
    #     return max(dfs(i - 1), dfs(i - 2) + nums[i])
    # return dfs(len(nums) - 1)

    # 数组优化
    # if len(nums) == 1:
    #     return nums[0]
    #
    # dp = [0] * len(nums)
    # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    #
    # for i in range(2, len(nums)):
    #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    # return dp[len(nums) - 1]

    # 临时变量优化
    f0 = f1 = 0
    for i in nums:
        f0, f1 = max(f0, f1 + i), f0
    return f0


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(func(nums))
