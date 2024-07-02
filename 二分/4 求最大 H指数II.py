# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午8:03
@Author  : zxy
@File    : 4 求最大 H指数II.py
"""
from mods import *

"""
https://leetcode.cn/problems/h-index-ii/
给你一个整数数组 citations ，
其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，
citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。
h 指数的定义：h 代表“高引用次数”（high citations），
一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。
"""


def func(citations: List[int]) -> int:
    n = len(citations)
    l, r = 1, n
    # l - 1指向是，r + 1指向否
    while l <= r:
        mid = l + (r - l) // 2
        if citations[-mid] >= mid:
            l = mid + 1
        else:
            r = mid - 1
    # l = r + 1
    return r  # l - 1


if __name__ == '__main__':
    citations = [0, 1, 3, 5, 6]
    print(func(citations))
