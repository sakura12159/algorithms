# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 下午2:56
@Author  : zxy
@File    : 3 交换字符串中的元素.py
"""
from mods import *

"""
https://leetcode.cn/problems/smallest-string-with-swaps/
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，
其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
"""


def func(s: str, pairs: List[List[int]]) -> str:
    l = len(s)
    par = {i: i for i in range(l)}

    def find(p):
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    def union(p1, p2):
        i1, i2 = find(p1), find(p2)
        if i1 != i2:
            par[i1] = i2

    for u, v in pairs:
        union(u, v)

    cnt = defaultdict(list)
    for i in range(l):
        cnt[find(i)].append(i)

    res = list(s)
    for i in cnt.values():
        for j, c in zip(i, sorted([res[idx] for idx in i])):  # 可交换的位置索引列表与以字典序排好的字母列表
            res[j] = c
    return "".join(res)


if __name__ == '__main__':
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    print(func(s, pairs))
