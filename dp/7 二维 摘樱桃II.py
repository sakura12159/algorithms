# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 15:44
@Author  : zxy
@File    : 7 二维 摘樱桃II.py
"""
from mods import *

"""
https://leetcode.cn/problems/cherry-pickup-ii/
给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。
你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。
请你按照如下规则，返回两个机器人能收集的最多樱桃数目：
    1 从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
    2 当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
    3 当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
    4 两个机器人在任意时刻都不能移动到 grid 外面。
    5 两个机器人最后都要到达 grid 最底下一行。
"""


def func(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    # 记忆化搜索
    # @cache
    # def dfs(i, j1, j2):
    #     def getValue(i, j1, j2):
    #         return grid[i][j1] + grid[i][j2] if j1 != j2 else grid[i][j1]
    #
    #     if i == m - 1:
    #         return getValue(i, j1, j2)
    #
    #     best = 0
    #     for dj1 in j1 - 1, j1, j1 + 1:
    #         for dj2 in j2 - 1, j2, j2 + 1:
    #             if 0 <= dj1 < n and 0 <= dj2 < n:
    #                 best = max(best, dfs(i + 1, dj1, dj2))
    #     return best + getValue(i, j1, j2)
    #
    # return dfs(0, 0, n - 1)

    # 数组递推
    # 定义 dp[i][j1][j2] 为当前走了 i 行，且第一个点当前在第 j1 列，第二点在第 j2 列时的最大得分，
    dp = [[[-inf for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][1][-1] = grid[0][0] + grid[0][-1]

    dirs = [1, 0, -1]
    for i in range(2, m + 1):
        for j1 in range(1, n + 1):
            for j2 in range(1, n + 1):
                cur = grid[i - 1][j1 - 1]
                if j1 != j2:
                    cur += grid[i - 1][j2 - 1]

                res = -inf
                for d1 in dirs:
                    new_j1 = j1 + d1
                    if 0 < new_j1 < n + 1:
                        for d2 in dirs:
                            new_j2 = j2 + d2
                            if 0 < new_j2 < n + 1:
                                res = max(res, cur + dp[i - 1][new_j1][new_j2])
                dp[i][j1][j2] = res

    ret = 0
    for row in dp[m]:
        ret = max(ret, max(row))
    return ret


if __name__ == '__main__':
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(func(grid))
