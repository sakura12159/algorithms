# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/3 下午1:48
@Author  : zxy
@File    : 12 分组背包 掷骰子的和等于目标数的方法数.py
"""
from mods import *

"""
分组背包：从每组物品中只多或恰好选一个
"""

"""
https://leetcode.cn/circle/discuss/tXLS3i/
这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
给定三个整数 n、k 和 target，请返回投掷骰子的所有可能得到的结果（共有 k ** n 种方式），
使得骰子面朝上的数字总和等于 target。
"""


def func(n: int, k: int, target: int) -> int:
    if target < n or target > k * n:
        return 0

    # 记忆化
    # @cache
    # def dfs(i, cur):
    #     if i < 1:
    #         return 1 if cur == 0 else 0
    #     res = 0
    #     for j in range(1, min(k, cur) + 1):
    #         res += dfs(i - 1, cur - j)
    #
    #     return res
    #
    # return dfs(n, target)

    # 二维递推
    # f = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    # f[0][0] = 1
    # for i in range(1, n + 1):
    #     for j in range(target + 1):
    #         for m in range(1, min(k, j) + 1):
    #             f[i][j] += f[i - 1][j - m]
    # return f[n][target]

    # 一维优化
    # 为了避免讨论 j < 0 的情况，可以把问题改成：
    # 每个骰子上的数字是 0 到 k - 1，数字之和是 target − n，
    # 相当于把每个骰子掷出的数字都提一个 1 出来，
    # 那么这些骰子的数字之和就等于 target − n
    f = [1] + [0] * (target - n)
    for i in range(1, n + 1):
        max_j = min(i * (k - 1), target - n)  # i个骰子至多掷出i * (k - 1)
        for j in range(1, max_j + 1):
            f[j] += f[j - 1]  # 计算前缀和
        for j in range(max_j, k - 1, -1):
            f[j] -= f[j - k]
    return f[target - n]


if __name__ == '__main__':
    n, k, target = 2, 6, 7
    print(func(n, k, target))
