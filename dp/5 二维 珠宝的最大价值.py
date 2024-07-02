# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 15:10
@Author  : zxy
@File    : 5 二维 珠宝的最大价值.py
"""
from mods import *

"""
https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/
现有一个记作二维矩阵 frame 的珠宝架，其中 frame[i][j] 为该位置珠宝的价值。拿取珠宝的规则为：
    1 只能从架子的左上角开始拿珠宝
    2 每次可以移动到右侧或下侧的相邻位置
    3 到达珠宝架子的右下角时，停止拿取
注意：珠宝的价值都是大于 0 的。
"""


def func(frames: List[List[int]]) -> int:
    # dfs(i, j) = frame[i][j] + max(dfs(i - 1, j)), dfs(i, j - 1)))
    m, n = len(frames), len(frames[0])
    # 记忆化搜索
    # @cache
    # def dfs(i, j):
    #     if i < 0 or j < 0:
    #         return 0
    #
    #     return frames[i][j] + max(dfs(i - 1, j), dfs(i, j - 1))
    # return dfs(m - 1, n - 1)

    # 二维数组优化
    # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # for i in range(m):
    #     for j in range(n):
    #         dp[i + 1][j + 1] = frames[i][j] + max(dp[i + 1][j], dp[i][j + 1])
    # return dp[m][n]

    # 一维数组优化
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            dp[j + 1] = frames[i][j] + max(dp[j + 1], dp[j])
    return dp[n]


if __name__ == '__main__':
    frames = [[1, 3, 1], [1, 5, 1], [4, 2, 1], [5, 3, 4]]
    print(func(frames))
