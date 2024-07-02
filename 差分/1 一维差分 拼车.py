# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午7:47
@Author  : zxy
@File    : 1 一维差分 拼车.py
"""
from mods import *

"""
https://leetcode.cn/problems/car-pooling/
车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 
表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。
这些位置是从汽车的初始位置向东的公里数。
当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
"""


def func(trips: List[List[int]], capacity: int) -> bool:
    # 写法 1
    # diff = [0] * 1001
    # for i, j, k in trips:
    #     diff[j] += i
    #     diff[k] -= i

    # res = 0
    # for i in diff:
    #     res += i
    #     if res > capacity:
    #         return False
    # return True

    # 写法 2
    d = [0] * 1001
    for num, from_, to in trips:
        d[from_] += num
        d[to] -= num
    return all(s <= capacity for s in accumulate(d))


if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print(func(trips, capacity))
