# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 上午9:01
@Author  : zxy
@File    : 4 按字典序排列最小的等效字符串.py
"""
from mods import *

"""
https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/
给出长度相同的两个字符串s1 和 s2 ，还有一个字符串 baseStr 。
其中  s1[i] 和 s2[i]  是一组等价字符。
举个例子，如果 s1 = "abc" 且 s2 = "cde"，那么就有 'a' == 'c', 'b' == 'd', 'c' == 'e'。
等价字符遵循任何等价关系的一般规则：
    1 自反性 ：'a' == 'a'
    2 对称性 ：'a' == 'b' 则必定有 'b' == 'a'
    3 传递性 ：'a' == 'b' 且 'b' == 'c' 就表明 'a' == 'c'
例如， s1 = "abc" 和 s2 = "cde" 的等价信息和之前的例子一样，那么 baseStr = "eed" , "acd" 或 "aab"，
这三个字符串都是等价的，而 "aab" 是 baseStr 的按字典序最小的等价字符串
利用 s1 和 s2 的等价信息，找出并返回 baseStr 的按字典序排列最小的等价字符串。
"""


def func(s1: str, s2: str, baseStr: str) -> str:
    par = [i for i in range(26)]

    def find(p):
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return par[p]

    def union(p1, p2):
        r1, r2 = find(p1), find(p2)
        # 谁的字典序小谁做父节点
        if r1 < r2:
            par[r2] = r1
        else:
            par[r1] = r2

    for i in range(len(s1)):
        union(ord(s1[i]) - 97, ord(s2[i]) - 97)

    res = ""
    for i in baseStr:
        res += chr(find(ord(i) - 97) + 97)
    return res


if __name__ == '__main__':
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(func(s1, s2, baseStr))
