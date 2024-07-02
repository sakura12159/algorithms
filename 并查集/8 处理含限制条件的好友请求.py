# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/11 下午3:40
@Author  : zxy
@File    : 8 处理含限制条件的好友请求.py
"""
from mods import *

"""
https://leetcode.cn/problems/process-restricted-friend-requests/
给你一个整数 n ，表示网络上的用户数目。每个用户按从 0 到 n - 1 进行编号。
给你一个下标从 0 开始的二维整数数组 restrictions ，
其中 restrictions[i] = [xi, yi] 意味着用户 xi 和用户 yi 不能 成为 朋友 ，不管是 直接 还是通过其他用户 间接 。
最初，用户里没有人是其他用户的朋友。给你一个下标从 0 开始的二维整数数组 requests 表示好友请求的列表，
其中 requests[j] = [uj, vj] 是用户 uj 和用户 vj 之间的一条好友请求。
如果 uj 和 vj 可以成为 朋友 ，那么好友请求将会 成功 。
每个好友请求都会按列表中给出的顺序进行处理（即，requests[j] 会在 requests[j + 1] 前）。
一旦请求成功，那么对所有未来的好友请求而言， uj 和 vj 将会 成为直接朋友 。
返回一个 布尔数组 result ，其中元素遵循此规则：如果第 j 个好友请求 成功 ，那么 result[j] 就是 true ；否则，为 false 。
注意：如果 uj 和 vj 已经是直接朋友，那么他们之间的请求将仍然 成功 。
"""


def func(n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
    par = [*range(n)]

    def find(p):
        if p != par[p]:
            par[p] = find(par[p])
        return par[p]

    rela = [[True for _ in range(n)] for _ in range(n)]
    for u, v in restrictions:
        rela[u][v] = rela[v][u] = False  # 双向

    res = [False] * len(requests)
    for i, (u, v) in enumerate(requests):
        r1, r2 = find(u), find(v)
        if not rela[r1][r2]:  # 如果无法成为朋友
            continue

        res[i] = True
        if r1 == r2:  # 已经是朋友
            continue

        if r1 > r2:  # 将小的集合合并到大的集合上，保证 r2 最大
            r1, r2 = r2, r1

        par[r1] = r2
        # 将 r1 的限制条件加到 r2 上去
        for j, rel in enumerate(rela[r1]):
            if not rel:
                rela[r2][j] = rela[j][r2] = False

    return res


if __name__ == '__main__':
    n = 3
    restrictions = [[0, 1]]
    requests = [[0, 2], [2, 1]]
    print(func(n, restrictions, requests))
