# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午1:06
@Author  : zxy
@File    : 4 不定长 长度最小的子数组.py
"""
from mods import *

"""
https://leetcode.cn/problems/minimum-size-subarray-sum/
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""


def func(target: int, nums: List[int]) -> int:
    # 在while内更新答案
    # l = len(nums)
    # cur = left = 0
    # ans = l + 1
    # for right, x in enumerate(nums):
    #     cur += x
    #     if cur >= target:
    #         while cur >= target:
    #             if right - left + 1 < ans:
    #                 ans = right - left + 1
    #             cur -= nums[left]
    #             left += 1
    # return ans if ans < l + 1 else 0

    # 在while结束后更新答案
    l = len(nums)
    ans = l + 1
    cur = left = 0
    for right, x in enumerate(nums):
        cur += x
        while cur - nums[left] >= target:
            cur -= nums[left]
            left += 1
        if cur >= target and right - left + 1 < ans:
            ans = right - left + 1
    return ans if ans < l + 1 else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(func(target, nums))
