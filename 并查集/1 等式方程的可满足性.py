# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 下午1:23
@Author  : zxy
@File    : 1 等式方程的可满足性.py
"""
from mods import *

"""
https://leetcode.cn/problems/satisfiability-of-equality-equations/
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。
"""


def func(equations: List[str]) -> bool:
    par = [i for i in range(26)]

    # 查
    # 递归写法，压缩完全，性能较差
    # def find(p):
    #     if p != par[p]:
    #         par[p] = find(par[p])
    #     return par[p]

    # 隔代压缩，压缩不完全，多次查询后可达到完全压缩，性能好
    def find(p):
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    # 并，合并两个集合
    def union(p1, p2):
        pp1, pp2 = find(p1), find(p2)
        par[pp1] = pp2

    # 判断根节点是否相同，本节点中如果两节点被赋予 != 时，根节点应不同
    def is_connected(p1, p2):
        return find(p1) == find(p2)

    for i in equations:
        u, eq, v = i[0], i[1], i[-1]
        if eq == '=':
            union(ord(u) - 97, ord(v) - 97)

    for i in equations:
        u, eq, v = i[0], i[1], i[-1]
        if eq == '!' and is_connected(ord(u) - 97, ord(v) - 97):
            return False
    return True
