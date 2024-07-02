# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/11 下午4:09
@Author  : zxy
@File    : 1 DFS + BFS + UF 省份数量.py
"""
from mods import *

"""
https://leetcode.cn/problems/number-of-provinces/
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，
且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
"""


def func(isConnected: List[List[int]]) -> int:
    n = len(isConnected)

    # DFS 写法，每次 dfs 标记当前节点连通的所有节点
    # vis = [False] * n
    # cnt = 0
    #
    # def dfs(i):
    #     vis[i] = True
    #     for j in range(n):
    #         if isConnected[i][j] and not vis[j]:
    #             dfs(j)
    #
    # for i in range(n):
    #     if not vis[i]:
    #         cnt += 1
    #         dfs(i)
    # return cnt

    # BFS 写法同理
    # vis = [False] * n
    # cnt = 0
    # dq = deque()
    # for i in range(n):
    #     if not vis[i]:
    #         cnt += 1
    #         dq.append(i)
    #         vis[i] = True
    #         while dq:
    #             nxt = dq.popleft()
    #             for j in range(n):
    #                 if isConnected[nxt][j] and not vis[j]:
    #                     dq.append(j)
    #                     vis[j] = True
    # return cnt

    # 并查集写法，统计连通块的数量
    class UnionFind:
        def __init__(self, n):
            self.par = [*range(n)]
            self.cnt = n

        def find(self, p):
            if p != self.par[p]:
                self.par[p] = self.find(self.par[p])
            return self.par[p]

        def union(self, p1, p2):
            r1, r2 = self.find(p1), self.find(p2)
            if r1 != r2:
                self.par[r1] = r2
                self.cnt -= 1

    uf = UnionFind(n)
    for i, x in enumerate(isConnected):
        for j, y in enumerate(x):
            if y:
                uf.union(i, j)
    return uf.cnt


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(func(isConnected))
