# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/3 上午10:49
@Author  : zxy
@File    : 11 多重背包 获得分数的方法数.py
"""
from mods import *

"""
多重背包：物品可以重复选，有个数限制
"""

"""
https://leetcode.cn/problems/number-of-ways-to-earn-points/
考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0 开始的二维整数数组 types，
其中 types[i] = [count, marks] 表示第 i 种类型的题目有 count 道，每道题目对应 marks 分。
返回你在考试中恰好得到 target 分的方法数。
注意，同类型题目无法区分。
"""


def func(types: List[List[int]], target: int) -> int:
    l = len(types)

    # 记忆化
    # @cache
    # def dfs(i, cur):
    #     if i < 0:
    #         return 1 if cur == 0 else 0
    #     res = 0
    #     c, m = types[i]
    #     for j in range(min(c, cur // m) + 1):
    #         res += dfs(i - 1, cur - j * m)
    #     return res
    #
    # return dfs(l - 1, target)

    # 二维递推
    # f = [[0 for _ in range(target + 1)] for _ in range(l + 1)]
    # f[0][0] = 1
    # for i, (c, m) in enumerate(types):
    #     for j in range(target + 1):
    #         for k in range(min(c, j // m) + 1):
    #             f[i + 1][j] += f[i][j - k * m]
    # return f[l][target]

    # 一维递推
    f = [1] + [0] * target
    for c, m in types:
        for i in range(target, 0, -1):
            for j in range(1, min(c, i // m) + 1):
                f[i] += f[i - j * m]
    return f[target]


if __name__ == '__main__':
    types = [[6, 1], [3, 2], [2, 3]]
    target = 6
    print(func(types, target))
