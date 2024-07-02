# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 上午10:22
@Author  : zxy
@File    : 5 执行交换操作后的最小汉明距离.py
"""
from mods import *

"""
https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/
给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，
其中每个 allowedSwaps[i] = [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。
注意，你可以按 任意 顺序 多次 交换一对特定下标指向的元素。
相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。
形式上，其值等于满足 source[i] != target[i] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。
在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。
"""


def func(source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    n = len(source)
    par = [*range(n)]

    def find(p):
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    def union(p1, p2):
        r1, r2 = find(p1), find(p2)
        if r1 != r2:
            par[r1] = r2

    # 根据 allowedSwaps 合并索引
    for i, j in allowedSwaps:
        union(i, j)

        # 按根节点分组索引
    groups = {}
    for i in range(n):
        root = find(i)
        if root in groups:
            groups[root].append(i)
        else:
            groups[root] = [i]

    # 计算最小汉明距离
    min_dis = 0
    for group in groups.values():
        # 统计 source 和 target 在当前分组中的元素频率
        sc, tc = {}, {}
        for i in group:
            sc[source[i]] = sc.get(source[i], 0) + 1
            tc[target[i]] = tc.get(target[i], 0) + 1
        # 对于当前分组，计算不能通过交换匹配的元素数量
        for val, count in sc.items():
            if count > tc.get(val, 0):
                min_dis += count - tc.get(val, 0)
    return min_dis


if __name__ == '__main__':
    source = [5, 1, 2, 4, 3]
    target = [1, 5, 4, 2, 3]
    allowedSwaps = [[0, 4], [4, 2], [1, 3], [1, 4]]
    print(func(source, target, allowedSwaps))
