# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/3 下午2:54
@Author  : zxy
@File    : 13 最长公共子序列LCS 正则表达式匹配.py
"""
from mods import *

"""
https://leetcode.cn/problems/regular-expression-matching/
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
    1 '.' 匹配任意单个字符
    2 '*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
"""


def func(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    # 记忆化
    # @cache
    # def dfs(i, j):
    #     if j >= n:
    #         return i >= m
    #     first_match = i < m and (p[j] == s[i] or p[j] == '.')
    #     res = first_match and dfs(i + 1, j + 1)
    #     if j < n - 1 and p[j + 1] == '*':
    #         res |= first_match and dfs(i + 1, j) or dfs(i, j + 2)
    #     return res
    #
    # return dfs(0, 0)

    # 二维递推
    f = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    f[0][0] = True
    for j in range(2, n + 1, 2):
        f[0][j] = f[0][j - 2] and p[j - 1] == "*"
        # 状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                f[i][j] = f[i][j - 2] or f[i - 1][j] and (s[i - 1] == p[j - 2] or  p[j - 2] == ".")
            else:
                f[i][j] = f[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
    return f[m][n]


if __name__ == '__main__':
    s, p = "aabba", "a.*a"
    print(func(s, p))
