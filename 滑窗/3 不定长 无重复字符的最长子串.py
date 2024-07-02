# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/4 下午6:48
@Author  : zxy
@File    : 3 不定长 无重复字符的最长子串.py
"""
from mods import *

"""
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
"""


def func(s: str) -> int:
    cnt = {}
    ans, j = 0, -1
    for i, x in enumerate(s):
        if x in cnt and cnt[x] > j:  # 记录上一个重复字符串出现的索引
            j = cnt[x]
        cnt[x] = i  # 记录最后一次出现的索引
        if i - j > ans:
            ans = i - j
    return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(func(s))
