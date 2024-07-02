# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/2 18:59
@Author  : zxy
@File    : 10 完全背包打印路径 数位成本和为目标值的最大数字.py
"""
from mods import *

"""
https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/
给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
    1 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
    2 总成本必须恰好等于 target 。
    3 添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。
如果按照上述要求无法得到任何整数，请你返回 "0" 。
"""


def func(cost: List[int], target: int) -> str:
    # 思路：先计算最多位数，位数多数必然大，然后从9-1遍历，
    # 如果当前状态能从前一个状态转移过来，就填入当前数字
    l = len(cost)

    # 记忆化搜索
    # @cache
    # def dfs(i, target):
    #     if i < 0:
    #         return 0 if target == 0 else -inf
    #     if target < cost[i]:
    #         return dfs(i - 1, target)
    #
    #     return max(dfs(i - 1, target), dfs(i, target - cost[i]) + 1)
    #
    # nums = dfs(l - 1, target)
    # if nums == -inf:
    #     return "0"
    #
    # res = ""
    # for i in range(9, 0, -1):
    #     c = cost[i - 1]
    #     while target >= c and dfs(l - 1, target) == dfs(l - 1, target - c) + 1:
    #         res += str(i)
    #         target -= c
    # return res

    # 递归
    f = [-inf] * (target + 1)
    f[0] = 0
    for i in cost:
        for j in range(i, target + 1):
            if f[j - i] + 1 > f[j]:
                f[j] = f[j - i] + 1

    if f[target] == -inf:
        return "0"

    res = ""
    for i in range(9, 0, -1):
        c = cost[i - 1]
        while target >= c and f[target] == f[target - c] + 1:  # 看是否能从当前状态转移至下一个状态
            res += str(i)
            target -= c
    return res


if __name__ == '__main__':
    cost = [4, 3, 2, 5, 6, 7, 2, 5, 5]
    target = 9
    print(func(cost, target))
