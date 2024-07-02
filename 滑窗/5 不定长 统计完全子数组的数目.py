# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午1:49
@Author  : zxy
@File    : 5 不定长 统计完全子数组的数目.py
"""
from mods import *

"""
https://leetcode.cn/problems/count-complete-subarrays-in-an-array/
给你一个由 正 整数组成的数组 nums 。
如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
    子数组中 不同 元素的数目等于整个数组不同元素的数目。
返回数组中 完全子数组 的数目。
子数组 是数组中的一个连续非空序列。
"""


def func(nums: List[int]) -> int:
    target = len(set(nums))
    ans = left = 0
    cnt = {}
    for x in nums:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
        while len(cnt) == target:
            cnt[nums[left]] -= 1
            if not cnt[nums[left]]:
                del cnt[nums[left]]
            left += 1
        ans += left  # 左侧的都是合法的
    return ans


if __name__ == '__main__':
    # nums = [1, 3, 1, 2, 2]
    nums = [5, 5, 5, 5, 5]
    print(func(nums))
