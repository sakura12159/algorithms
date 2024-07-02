# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 15:28
@Author  : zxy
@File    : 6 二维 摘樱桃I.py
"""
from mods import *

"""
https://leetcode.cn/problems/cherry-pickup/
给你一个 n x n 的网格 grid ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：
    0 表示这个格子是空的，所以你可以穿过它。
    1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
    -1 表示这个格子里有荆棘，挡着你的路。
请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：
    1 从位置 (0, 0) 出发，最后到达 (n - 1, n - 1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 0 或者 1 的格子）；
    2 当到达 (n - 1, n - 1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
    3 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 0 ）；
    4 如果在 (0, 0) 和 (n - 1, n - 1) 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。
"""


def func(grid: List[List[int]]):
    n = len(grid)
    # 本题应看作是两个人同时从左上角起点出发至右下角，两人能够采到的樱桃数的最大值

    # 记忆化搜索
    # dirs = [[1, 0], [0, 1]]

    # 4维
    # @cache
    # def dfs(x1, y1, x2, y2):
    #     if x1 == n - 1 and y1 == n - 1:
    #         return grid[n - 1][n - 1]
    #
    #     res, cur = -inf, grid[x1][y1]
    #     if x1 != x2 or y1 != y2:
    #         cur += grid[x2][y2]
    #
    #     for i in dirs:
    #         new_x1, new_y1 = x1 + i[0], y1 + i[1]
    #         if 0 <= new_x1 < n and 0 <= new_y1 < n and grid[new_x1][new_y1] != -1:
    #             for j in dirs:
    #                 new_x2, new_y2 = x2 + j[0], y2 + j[1]
    #                 if 0 <= new_x2 < n and 0 <= new_y2 < n and grid[new_x2][new_y2] != -1:
    #                     res = max(res, cur + dfs(new_x1, new_y1, new_x2, new_y2))
    #     return res
    #
    # return max(0, dfs(0, 0, 0, 0))

    # 由于两人必在一条对角线上，即x1 + y1 = x2 + y2，可压缩一个维度
    # dirs = [[1, 0], [0, 1]]

    # 3维
    # @cache
    # def dfs(x1, y1, x2):
    #     if x1 == n - 1 and y1 == n - 1:
    #         return grid[n - 1][n - 1]
    #
    #     y2 = x1 + y1 - x2
    #     res, cur = -inf, grid[x1][y1]
    #     if x1 != x2 or y1 != y2:
    #         cur += grid[x2][y2]
    #
    #     for i in dirs:
    #         new_x1, new_y1 = x1 + i[0], y1 + i[1]
    #         if 0 <= new_x1 < n and 0 <= new_y1 < n and grid[new_x1][new_y1] != -1:
    #             for j in dirs:
    #                 new_x2, new_y2 = x2 + j[0], y2 + j[1]
    #                 if 0 <= new_x2 < n and 0 <= new_y2 < n and grid[new_x2][new_y2] != -1:
    #                     res = max(res, cur + dfs(new_x1, new_y1, new_x2))
    #     return res
    #
    # return max(0, dfs(0, 0, 0))

    # 三维数组优化
    # f = [[[-inf for _ in range(n)] for _ in range(n)] for _ in range(n * 2 - 1)]
    # f[0][0][0] = grid[0][0]
    # for k in range(1, n * 2 - 1):
    #     for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
    #         y1 = k - x1
    #         if grid[x1][y1] == -1:
    #             continue
    #         for x2 in range(x1, min(k + 1, n)):
    #             y2 = k - x2
    #             if grid[x2][y2] == -1:
    #                 continue
    #             res = f[k - 1][x1][x2]  # 都往右
    #             if x1:
    #                 res = max(res, f[k - 1][x1 - 1][x2])  # 往下，往右
    #             if x2:
    #                 res = max(res, f[k - 1][x1][x2 - 1])  # 往右，往下
    #             if x1 and x2:
    #                 res = max(res, f[k - 1][x1 - 1][x2 - 1])  # 都往下
    #             res += grid[x1][y1]
    #             if x2 != x1:  # 避免重复摘同一个樱桃
    #                 res += grid[x2][y2]
    #             f[k][x1][x2] = res
    # return max(0, f[2 * n - 2][n - 1][n - 1])

    # 二维数组倒序优化
    f = [[-inf for _ in range(n)] for _ in range(n)]
    f[0][0] = grid[0][0]
    for k in range(1, n * 2 - 1):
        for x1 in range(min(k, n - 1), max(k - n, -1), -1):
            for x2 in range(min(k, n - 1), x1 - 1, -1):
                y1, y2 = k - x1, k - x2
                if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                    f[x1][x2] = -inf
                    continue
                res = f[x1][x2]  # 都往右
                if x1:
                    res = max(res, f[x1 - 1][x2])  # 往下，往右
                if x2:
                    res = max(res, f[x1][x2 - 1])  # 往右，往下
                if x1 and x2:
                    res = max(res, f[x1 - 1][x2 - 1])  # 都往下
                res += grid[x1][y1]
                if x2 != x1:  # 避免重复摘同一个樱桃
                    res += grid[x2][y2]
                f[x1][x2] = res
    return max(0, f[n - 1][n - 1])


if __name__ == '__main__':
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    print(func(grid))
