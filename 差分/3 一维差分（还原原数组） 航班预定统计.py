# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午9:44
@Author  : zxy
@File    : 3 一维差分（还原原数组） 航班预定统计.py
"""
from mods import *

"""
https://leetcode.cn/problems/corporate-flight-bookings/
这里有 n 个航班，它们分别从 1 到 n 进行编号。
有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 
意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
"""


def func(bookings: List[List[int]], n: int) -> List[int]:
    diff = [0] * n
    for f, l, s in bookings:
        diff[f - 1] += s
        if l < n:
            diff[l] -= s

    for i in range(1, n):
        diff[i] += diff[i - 1]
    return diff


if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(func(bookings, n))
