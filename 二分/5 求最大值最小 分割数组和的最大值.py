# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午9:30
@Author  : zxy
@File    : 5 求最大值最小 分割数组和的最大值.py
"""
from mods import *

"""
https://leetcode.cn/problems/split-array-largest-sum/
给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组。
设计一个算法使得这 k 个子数组各自和的最大值最小。
"""


def func(nums: List[int], k: int) -> int:
    def check(mx):
        cnt, s = 1, 0  # 段数 当前段数和
        for x in nums:
            if s + x <= mx:
                s += x
            else:  # 单独划分一段
                if cnt == k:
                    return False
                cnt += 1
                s = x
        return True

    r = sum(nums) - 1
    l = max(max(nums), r // k)
    # 双闭区间
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2
    print(func(nums, k))
