# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午2:38
@Author  : zxy
@File    : 7 带权并查集.py
"""
from mods import *

"""
https://leetcode.cn/problems/evaluate-division/
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，
请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。
"""


class UnionFind:
    def __init__(self, n):
        self.par = [*range(n)]
        self.weig = [1.] * n

    # 隔代压缩
    def find(self, p):
        if p != self.par[p]:
            tmp = self.par[p]
            self.par[p] = self.find(self.par[p])  # 更新父节点
            self.weig[p] *= self.weig[tmp]  # 更新权重
        return self.par[p]

    def union(self, p1, p2, v):
        r1, r2 = self.find(p1), self.find(p2)
        if r1 != r2:
            self.par[r1] = r2
            # self.weig[p1] * self.weig[r1] = self.weig[p2] * v
            self.weig[r1] = self.weig[p2] * v / self.weig[p1]  # 关键

    def is_connect(self, p1, p2):
        """判断是否属于一个连通量"""
        return self.weig[p1] / self.weig[p2] if self.find(p1) == self.find(p2) else -1.


def func(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    uf = UnionFind(2 * len(equations))  # 最多不超过 2 * n 个变量

    hs = {}
    # 映射变量值到 idx ，作为合并与查找的输入
    idx = 0
    for i, (u, v) in enumerate(equations):
        if u not in hs:
            hs[u] = idx
            idx += 1
        if v not in hs:
            hs[v] = idx
            idx += 1
        uf.union(hs[u], hs[v], values[i])

    m = len(queries)
    res = [-1.] * m
    for i, (u, v) in enumerate(queries):
        if u in hs and v in hs:
            res[i] = uf.is_connect(hs[u], hs[v])  # 判断是否属于同一个连通量
    return res


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(func(equations, values, queries))
