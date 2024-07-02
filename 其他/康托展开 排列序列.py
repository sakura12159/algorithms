# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 上午9:09
@Author  : zxy
@File    : 康托展开 排列序列.py
"""
from mods import *

"""
https://leetcode.cn/problems/permutation-sequence/
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
    1 "123"
    2 "132"
    3 "213"
    4 "231"
    5 "312"
    6 "321"
给定 n 和 k，返回第 k 个排列。
"""


def func(n: int, k: int) -> str:
    # 模拟
    # fac = [1]
    # for i in range(1, n + 1):
    #     fac.append(fac[i - 1] * i)  # 计算阶乘
    #
    # vis = [False] * (n + 1)  # 记录使用过的数字
    # ans = ""
    # for i in range(n - 1, -1, -1):
    #     cur = fac[i]  # 当前分支能够产生的节点数
    #     for j in range(1, n + 1):
    #         if vis[j]:
    #             continue
    #         if k > cur:  # 如果当前分支节点数小于 k ，跳过当前分支并减去当前分支能够产生的节点总数
    #             k -= cur
    #             continue
    #         vis[j] = True
    #         ans += str(j)
    #         break
    # return ans

    # 数学 康托展开
    fac = [1]
    for i in range(1, n + 1):
        fac.append(fac[i - 1] * i)  # 计算阶乘

    k -= 1
    res = ""
    nums = [i for i in range(1, n + 1)]
    for i in range(n - 1, -1, -1):
        idx = k // fac[i]
        k %= fac[i]
        res += str(nums[idx])
        nums = nums[:idx] + nums[idx + 1:]
    return res


if __name__ == '__main__':
    n, k = 6, 373
    print(func(n, k))
