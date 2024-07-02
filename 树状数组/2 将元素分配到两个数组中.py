# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/10 上午10:00
@Author  : zxy
@File    : 2 将元素分配到两个数组中.py
"""
from mods import *

"""
https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/
给你一个下标从 1 开始、长度为 n 的整数数组 nums 。
现定义函数 greaterCount ，使得 greaterCount(arr, val) 返回数组 arr 中 严格大于 val 的元素数量。
你需要使用 n 次操作，将 nums 的所有元素分配到两个数组 arr1 和 arr2 中。在第一次操作中，
将 nums[1] 追加到 arr1 。在第二次操作中，将 nums[2] 追加到 arr2 。之后，在第 i 次操作中：
    1 如果 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr1 。
    2 如果 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]) ，将 nums[i] 追加到 arr2 。
    3 如果 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]) ，将 nums[i] 追加到元素数量较少的数组中。
如果仍然相等，那么将 nums[i] 追加到 arr1 。
连接数组 arr1 和 arr2 形成数组 result 。例如，如果 arr1 == [1,2,3] 且 arr2 == [4,5,6] ，
那么 result = [1,2,3,4,5,6] 。
返回整数数组 result 。
"""


class TreeArray:
    __slots__ = 'tree'

    def __init__(self, n):
        self.tree = [0] * n

    @staticmethod
    def _lowbit(i):
        return i & -i

    def add(self, i):
        """将下标为i的元素增加1"""
        while i < len(self.tree):
            self.tree[i] += 1
            i += self._lowbit(i)

    def pre_sum(self, i):
        """返回[1, i]间的元素之和"""
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= self._lowbit(i)
        return ans


def lower_bound(nums, v):
    """返回第一个严格大于v的元素索引"""
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > v:
            r = mid - 1
        else:
            l = mid + 1
    return l


def func(nums: List[int]) -> List[int]:
    sorted_nums = sorted(set(nums))  # 离散化
    m = len(sorted_nums)
    a, b = [nums[0]], [nums[1]]
    t1, t2 = TreeArray(m + 1), TreeArray(m + 1)
    t1.add(lower_bound(sorted_nums, nums[0]))
    t2.add(lower_bound(sorted_nums, nums[1]))
    for x in nums[2:]:
        idx = lower_bound(sorted_nums, x)
        gc1, gc2 = len(a) - t1.pre_sum(idx), len(b) - t2.pre_sum(idx)
        if gc1 > gc2 or gc1 == gc2 and len(a) <= len(b):
            a.append(x)
            t1.add(idx)
        else:
            b.append(x)
            t2.add(idx)
    return a + b


if __name__ == '__main__':
    nums = [5, 14, 3, 1, 2]
    print(func(nums))
