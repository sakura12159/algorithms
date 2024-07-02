# -*- coding: utf-8 -*-
"""
@Time    : 2024/6/26 上午8:52
@Author  : zxy
@File    : 1 状态压缩dp 优美的排列.py
"""
from mods import *

"""
https://leetcode.cn/problems/beautiful-arrangement/
假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：
    1 perm[i] 能够被 i 整除
    2 i 能够被 perm[i] 整除
给你一个整数 n ，返回可以构造的 优美排列 的 数量 。
"""


def func(n: int) -> int:
    # 1 记忆化 正向
    # u = (1 << n) - 1
    #
    # @cache
    # def dfs(i):
    #     if i == u:  # 当所有元素都选过
    #         return 1
    #
    #     res = 0
    #     idx = i.bit_count() + 1  # 当前集合大小
    #     for j in range(1, n + 1):
    #         if i >> (j - 1) & 1 == 0 and (j % idx == 0 or idx % j == 0):  # 如果当前元素没选过且满足条件
    #             res += dfs(i | (1 << (j - 1)))
    #     return res
    #
    # return dfs(0)

    # 记忆化 反向
    # @cache
    # def dfs(i):
    #     if not i:  # 当所有元素都选过
    #         return 1
    #
    #     res = 0
    #     idx = i.bit_count()  # 当前集合大小
    #     for j in range(1, n + 1):
    #         if i >> (j - 1) & 1 and (j % idx == 0 or idx % j == 0):  # 如果当前元素没选过且满足条件
    #             res += dfs(i ^ (1 << (j - 1)))
    #     return res
    #
    # return dfs((1 << n) - 1)

    # 2 递推
    u = 1 << n
    f = [0] * u
    f[0] = 1
    for i in range(1, u):
        idx = i.bit_count()
        for j in range(1, n + 1):
            if i >> (j - 1) & 1 and (j % idx == 0 or idx % j == 0):  # 如果当前元素没选过且满足条件
                f[i] += f[i ^ (1 << (j - 1))]
    return f[-1]


if __name__ == '__main__':
    print(func(3))
