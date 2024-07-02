# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 上午11:18
@Author  : zxy
@File    : 8 求第K大 找出数组的第K大和.py
"""
from mods import *

"""
https://leetcode.cn/problems/find-the-k-sum-of-an-array/
给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
返回数组的 第 k 大和 。
子序列是一个可以由其他数组删除某些或不删除元素派生而来的数组，且派生过程不改变剩余元素的顺序。
注意：空子序列的和视作 0 。
"""


def func(nums: List[int], k: int) -> int:
    s = 0
    n = len(nums)
    # 原来nums中任意一个子序列和等价于从正数和中减去某些非负数或加上某些负数，
    # 即减去nums[i]的绝对值，因此从正数和中减去的数越小，nums的子序列和越大
    for i, x in enumerate(nums):  # 求正数的和s
        if x >= 0:
            s += x
        else:
            nums[i] = -x  # 将负数取绝对值
    nums.sort()

    # 原问题为子序列的k大和
    # 现在问题转化为，nums中的第k小子序列和，用正数和去减k小和即得到答案

    def check(sl):
        """是否能找到k个子序列和不超过sl的子序列"""
        cnt = 1  # 空的子序列

        def dfs(i, s):
            nonlocal cnt
            if cnt == k or i == n or s + nums[i] > sl:  # 已经找到 / 超索引也找不到 / 子序列和过大，找不到
                return
            cnt += 1
            dfs(i + 1, s + nums[i])  # 选择当前元素
            dfs(i + 1, s)  # 不选当前元素

        dfs(0, 0)
        return cnt == k

    l, r = 0, sum(nums)
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    return s - l


if __name__ == '__main__':
    nums = [1, -2, 3, 4, -10, 12]
    k = 16
    print(func(nums, k))
