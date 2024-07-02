# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 18:37
@Author  : zxy
@File    : 9 完全背包 零钱兑换.py
"""
from mods import *

"""
完全背包：每个物品能选任意次
"""

"""
https://leetcode.cn/problems/coin-change/
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
每种硬币的数量是无限的。
"""


def func(coins: List[int], amount: int) -> int:
    l = len(coins)

    # 记忆化搜索
    # @cache
    # def dfs(i, cur):
    #     if i < 0:
    #         return 0 if cur == 0 else inf
    #     if cur < coins[i]:
    #         return dfs(i - 1, cur)
    #     return min(dfs(i - 1, cur), dfs(i, cur - coins[i]) + 1)
    # res = dfs(l - 1, amount)
    # return res if res < inf else -1

    # 二维递推
    # f = [[inf for _ in range(amount + 1)] for _ in range(l + 1)]
    # f[0][0] = 0
    # for i in range(l):
    #     for j in range(amount + 1):
    #         f[i + 1][j] = f[i][j]
    #         if j >= coins[i]:
    #             f[i + 1][j] = min(f[i + 1][j], f[i + 1][j - coins[i]] + 1)
    # return f[l][amount] if f[l][amount] < inf else -1

    f = [inf] * (amount + 1)
    f[0] = 0
    for i in coins:
        for j in range(i, amount + 1):  # 不用倒序，同一行（i + 1）状态转移来的
            f[j] = min(f[j], f[j - i] + 1)
    return f[amount] if f[amount] < inf else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 15
    print(func(coins, amount))
