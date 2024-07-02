# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午12:42
@Author  : zxy
@File    : 6 情侣牵手.py
"""
from mods import *

"""
https://leetcode.cn/problems/couples-holding-hands/
n 对情侣坐在连续排列的 2n 个座位上，想要牵到对方的手。
人和座位由一个整数数组 row 表示，其中 row[i] 是坐在第 i 个座位上的人的 ID。
情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2n-2, 2n-1)。
返回 最少交换座位的次数，以便每对情侣可以并肩坐在一起。 每次交换可选择任意两人，让他们站起来交换座位。
"""


def func(row: List[int]) -> int:
    l = len(row)
    l2 = l // 2
    par = [*range(l2)]  # 情侣对编号

    def find(p):
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    def union(p1, p2):
        r1, r2 = find(p1), find(p2)
        if r1 != r2:
            par[r1] = r2

    for i in range(0, l, 2):
        union(row[i] // 2, row[i + 1] // 2)  # 连通相邻的两个人

    cnt = 0
    for i in range(l2):
        cnt += i != find(i)  # 统计情侣对编号错误的数量
    return cnt


if __name__ == '__main__':
    row = [0, 2, 1, 3]
    print(func(row))
