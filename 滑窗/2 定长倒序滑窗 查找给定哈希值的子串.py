# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/4 下午4:22
@Author  : zxy
@File    : 2 定长倒序滑窗 查找给定哈希值的子串.py
"""
from mods import *

"""
https://leetcode.cn/problems/find-substring-with-given-hash-value/
给定整数 p 和 m ，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算：
    hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26 。
给你一个字符串 s 和整数 power，modulo，k 和 hashValue 。请你返回 s 中 第一个 长度为 k 的 子串 sub，
满足 hash(sub, power, modulo) == hashValue。
子串 定义为一个字符串中连续非空字符组成的序列。
"""


def func(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    n = len(s)
    # 用秦九韶算法计算 s[n-k:] 的哈希值
    # ord(c) & 31 == ord(c) - 96，都将a-z映射到1-26
    _hash = 0
    for i in range(n - 1, n - k - 1, -1):
        _hash = (_hash * power + (ord(s[i]) & 31)) % modulo
    ans = n - k if _hash == hashValue else 0
    pk = pow(power, k, modulo)  # 计算要从滑窗中删除的power ^ k项
    # 倒序滑窗
    for i in range(n - k - 1, -1, -1):
        # 计算新的哈希值
        _hash = (_hash * power + (ord(s[i]) & 31) - pk * (ord(s[i + k]) & 31)) % modulo  # 加进入滑窗字符对应的项，减弹出滑窗字符对应的项
        if _hash == hashValue:
            ans = i
    return s[ans: ans + k]


if __name__ == '__main__':
    s = "leetcode"
    power, modulo, k, hashValue = 7, 20, 2, 0
    print(func(s, power, modulo, k, hashValue))