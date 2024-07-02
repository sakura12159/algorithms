# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午3:14
@Author  : zxy
@File    : 6 不定长多指针 和相同的二元子数组.py
"""
from mods import *

"""
https://leetcode.cn/problems/binary-subarrays-with-sum/
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。
"""


def func(nums: List[int], goal: int) -> int:
    # 前缀和 + 哈希表
    # 0 - r 与 0 - （l - 1）的差值为l - r的子数组和，用hash记录出现的次数
    # n = len(nums)
    # pre_sum = [0] * n
    # pre_sum[0] = nums[0]
    # for i in range(1, n):
    #     pre_sum[i] = pre_sum[i - 1] + nums[i]
    # mem = {0: 1}  # 两段之差为0时说明当前子数组符合条件
    #
    # ans = 0
    # for i in range(n):
    #     cur_sum = pre_sum[i]
    #     target = cur_sum - goal  # 两段差值
    #     ans += mem.get(target, 0)
    #     if cur_sum in mem:  # 记录差值出现的次数
    #         mem[cur_sum] += 1
    #     else:
    #         mem[cur_sum] = 1
    # return ans

    # 多指针
    n = len(nums)
    ans = l1 = l2 = s1 = s2 = 0
    for r in range(n):
        s1 += nums[r]
        s2 += nums[r]
        while l1 <= r and s1 > goal:
            s1 -= nums[l1]
            l1 += 1
        while l2 <= r and s2 >= goal:
            s2 -= nums[l2]
            l2 += 1
        ans += l2 - l1
    return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(func(nums, goal))
