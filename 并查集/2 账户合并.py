# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 下午2:13
@Author  : zxy
@File    : 2 账户合并.py
"""
from mods import *

"""
https://leetcode.cn/problems/accounts-merge/
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，
其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。
一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，
其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。
"""


def func(accounts: List[List[str]]) -> List[List[str]]:
    l = len(accounts)
    par = [i for i in range(l)]  # 代表 name 的索引
    addrs = {}  # key 是 mail 地址，value 是所属 name 的索引

    def find(p):
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    def union(p1, p2):
        par[find(p1)] = find(p2)

    for i in range(l):
        for j in range(1, len(accounts[i])):
            addr = accounts[i][j]
            if addr in addrs:
                union(i, addrs[addr])  # 合并 name
            else:
                addrs[addr] = i

    un = defaultdict(list)
    for k, v in addrs.items():
        un[find(v)].append(k)  # 根据根 name 索引合并每个 name 对应的所有 mail 地址

    res = []
    for k, v in un.items():
        res.append([accounts[k][0]] + sorted(v))
    return res


if __name__ == '__main__':
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]
    ]
    print(func(accounts))
