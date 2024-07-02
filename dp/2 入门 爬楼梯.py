# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 13:53
@Author  : zxy
@File    : 2 入门 爬楼梯.py
"""
from mods import *

"""
https://leetcode.cn/problems/climbing-stairs
假设你正在爬楼梯。需要 n 阶你才能到达楼顶，每次你可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶？
"""


def func(n: int) -> int:
    # dfs(i) = dfs(i - 1) + dfs(i - 2)

    # 记忆化递归
    # @cache
    # def dfs(i):
    #     if i <= 1:
    #         return 1
    #
    #     return dfs(i - 1) + dfs(i - 2)
    # return dfs(n)

    # 数组优化
    # dp = [0] * (n + 1)
    # dp[0] = dp[1] = 1
    #
    # for i in range(2, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    # return dp[n]

    # 临时变量优化
    f0 = f1 = 1
    for i in range(2, n + 1):
        tmp = f0 + f1
        f0, f1 = f1, tmp
    return f1


if __name__ == '__main__':
    n = 10
    print(func(n))
