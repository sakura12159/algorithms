# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 15:53
@Author  : zxy
@File    : 8 01背包 和为目标值的最长子序列.py
"""
from mods import *

"""
01背包：每个物品只能选一次
"""

"""
https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/
给你一个下标从 0 开始的整数数组 nums 和一个整数 target。
返回和为 target 的 nums 子序列中，子序列 长度的最大值 。如果不存在和为 target 的子序列，返回 -1 。
子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。
"""


def func(nums: List[int], target: int) -> int:
    l = len(nums)

    # 记忆化搜索
    # @cache
    # def dfs(i, target):
    #     if i < 0:
    #         return 0 if target == 0 else -inf
    #     if target < nums[i]:
    #         return dfs(i - 1, target)
    #     return max(dfs(i - 1, target), dfs(i - 1, target - nums[i]) + 1)
    #
    # res = dfs(l - 1, target)
    # return res if res else -1

    # 二维递推
    # f = [[-inf for _ in range(target + 1)] for _ in range(l + 1)]
    # f[0][0] = 0
    # for i in range(l):
    #     for j in range(target + 1):
    #         if j >= nums[i]:
    #             f[i + 1][j] = max(f[i][j], f[i][j - nums[i]] + 1)
    #         else:
    #             f[i + 1][j] = f[i][j]
    # return f[l][target] if f[l][target] > 0 else -1

    # 两个一维数组 + 前缀和优化
    # f = [[-inf for _ in range(target + 1)] for _ in range(2)]
    # f[0][0] = 0
    # s = 0
    # for i in range(len(nums)):
    #     f[i % 2][0], s = 0, min(s + nums[i], target)
    #     for j in range(1, s + 1):
    #         if j >= nums[i]:
    #             f[(i + 1) % 2][j] = max(f[i % 2][j], f[i % 2][j - nums[i]] + 1)
    #         else:
    #             f[(i + 1) % 2][j] = f[i % 2][j]
    #
    # return f[l % 2][target] if f[l % 2][target] > 0 else -1

    # 一维数组 + 前缀和优化
    f = [-inf for _ in range(target + 1)]
    f[0] = s = 0  # s为前i个数的和的与target间的最小值，便于缩小j的遍历范围
    for i in nums:
        s = min(s + i, target)
        for j in range(s, i - 1, -1):
            if f[j - i] + 1 > f[j]:  # 倒序，因为状态i + 1, j + 1从i, j转移过来
                f[j] = f[j - i] + 1

    return f[target] if f[target] > 0 else -1


if __name__ == '__main__':
    nums = [4, 1, 3, 2, 1, 5]
    target = 7
    print(func(nums, target))
