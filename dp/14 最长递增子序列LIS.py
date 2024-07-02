# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/3 下午3:33
@Author  : zxy
@File    : 14 最长递增子序列LIS.py
"""
from mods import *

"""
https://leetcode.cn/problems/longest-increasing-subsequence/
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""


def func(nums: List[int]) -> int:
    n = len(nums)

    # 记忆化
    # @cache
    # def dfs(i):
    #     res = 0
    #     for j in range(i):
    #         if nums[j] < nums[i]:
    #             res = max(res, dfs(j))
    #     return res + 1

    # res = 0
    # for i in range(n):
    #     res = max(res, dfs(i))
    # return res

    # 递推
    # f = [0] * n
    # for i in range(n):
    #     for j in range(i):
    #         if nums[j] < nums[i] and f[j] > f[i]:
    #             f[i] = f[j]
    #     f[i] += 1
    # return max(f)

    # 贪心 + 二分
    # 如果严格递增，则二分查找第一个大于等于目标值的元素，即左边界；非严格递增则查找最后一个小于等于目标值的元素，即右边界
    def bi_left(res, val):
        l, r = 0, len(res)
        while l < r:
            mid = l + (r - l) // 2
            if res[mid] >= val:
                r = mid
            else:
                l = mid + 1
        return l

    res = []
    for x in nums:
        idx = bi_left(res, x)
        if idx == len(res):
            res.append(x)
        else:
            res[idx] = x
    return len(res)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(func(nums))
