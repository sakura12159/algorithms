# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/9 下午3:55
@Author  : zxy
@File    : 1 区域和检索.py
"""
from mods import *

"""
https://leetcode.cn/problems/range-sum-query-mutable/
给你一个数组 nums ，请你完成两类查询。
其中一类查询要求 更新 数组 nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：
    1 NumArray(int[] nums) 用整数数组 nums 初始化对象
    2 void update(int index, int val) 将 nums[index] 的值 更新 为 val
    3 int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 
    （即，nums[left] + nums[left + 1], ..., nums[right]）
"""


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        # self.nums = [0] * n
        # self.tree = [0] * (n + 1)
        # for i, x in enumerate(nums):
        #     self.update(i, x)

        # 优化
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1):  # i 从 1 开始
            tree[i] += x
            nxt = i + self._lowbit(i)  # 下一个关键区间的右端点
            if nxt <= n:
                tree[nxt] += tree[i]
        self.nums = nums
        self.tree = tree

    @staticmethod
    def _lowbit(index: int) -> int:
        return index & -index

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val  # 更新修改的值
        i = index + 1  # 起始从 1 开始，到 n 结束
        while i < len(self.tree):
            self.tree[i] += delta  # 修改受影响的所有右端点
            i += self._lowbit(i)  # 下一个右端点

    def preSum(self, index: int) -> int:
        # 计算前缀 [1, index] 的元素和
        s = 0
        while index:  # 到 0 结束
            s += self.tree[index]  # 计算 [i - lowbit(i) + 1, i] 的元素和
            index -= self._lowbit(index)  # 下一个关键区间的右端点
        return s

    def sumRange(self, left: int, right: int) -> int:
        # 返回 [1, left] 至 [1, right + 1] 元素和之差
        return self.preSum(right + 1) - self.preSum(left)


if __name__ == '__main__':
    nums = [1 for _ in range(10)]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
