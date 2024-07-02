# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午4:38
@Author  : zxy
@File    : 3 求最小 使结果不超过阈值的最小除数.py
"""
from mods import *

"""
https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/
给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。
请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。
每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。
"""


def func(nums: List[int], threshold: int) -> int:
    l, r = 1, max(nums) + 1
    while l < r:
        mid = l + (r - l) // 2
        if sum((i - 1) // mid + 1 for i in nums) <= threshold:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = [2, 3, 5, 7, 11]
    threshold = 11
    print(func(nums, threshold))
