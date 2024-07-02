# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/3 下午6:46
@Author  : zxy
@File    : 1 定长 定长子串中元音的最大数目.py
"""
from mods import *

"""
https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
给你字符串 s 和整数 k 。
请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
英文中的 元音字母 为（a, e, i, o, u）。
"""


def func(s: str, k: int) -> int:
    v = "aeiou"
    count = 0
    for i in s[:k]:
        if i in v:
            count += 1

    mx = count
    l, r = 0, k
    while r < len(s):
        count = count - (s[l] in v) + (s[r] in v)
        if count > mx:
            mx = count
        l += 1
        r += 1
    return mx


if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    print(func(s, k))
