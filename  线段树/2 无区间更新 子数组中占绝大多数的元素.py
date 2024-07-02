# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/28 上午10:05
@Author  : zxy
@File    : 2 无区间更新 子数组中占绝大多数的元素.py
"""
from mods import *

"""
https://leetcode.cn/problems/online-majority-element-in-subarray/
设计一个数据结构，有效地找到给定子数组的 多数元素 。
子数组的 多数元素 是在子数组中出现 threshold 次数或次数以上的元素。
实现 MajorityChecker 类:
    1 MajorityChecker(int[] arr) 会用给定的数组 arr 对 MajorityChecker 初始化。
    2 int query(int left, int right, int threshold) 返回子数组中的元素  arr[left...right] 至少出现 threshold 次数，
    如果不存在这样的元素则返回 -1。
"""


class Node:
    """节点"""

    def __init__(self):
        self.l = 0  # 左端点
        self.r = 0  # 右端点
        self.val = 0  # 候选众数
        self.cnt = 0  # 候选众数的出现次数


class SegmentTree:
    """线段树"""

    def __init__(self, arr: List[int]):
        n = len(arr)
        self.arr = arr
        self.tree = [Node() for _ in range(n << 2)]  # 4n 个节点
        self._build(1, 1, n)

    def _build(self, val: int, l: int, r: int) -> None:
        """
        递归建树
        Args:
            val: 候选众数
            l: 节点左端点
            r: 节点右端点

        Returns:

        """
        self.tree[val].l = l
        self.tree[val].r = r

        if l == r:
            self.tree[val].val = self.arr[l - 1]
            self.tree[val].cnt = 1
            return

        mid = (l + r) >> 1
        self._build(val << 1, l, mid)
        self._build(val << 1 | 1, mid + 1, r)
        self._pushup(val)

    def _pushup(self, val: int) -> None:
        """
        向上更新，这里更新父节点的候选众数和出现次数
        Args:
            val: 候选众数

        Returns:

        """
        # 叶子结点候选众数相等，次数相加
        if self.tree[val << 1].val == self.tree[val << 1 | 1].val:
            self.tree[val].val = self.tree[val << 1].val
            self.tree[val].cnt = self.tree[val << 1].cnt + self.tree[val << 1 | 1].cnt
        # 叶子节点候选众数不等，选择大的更新父节点各值
        else:
            if self.tree[val << 1].cnt > self.tree[val << 1 | 1].cnt:
                self.tree[val].cnt = self.tree[val << 1].cnt - self.tree[val << 1 | 1].cnt
            else:
                self.tree[val].cnt = self.tree[val << 1 | 1].cnt - self.tree[val << 1].cnt

    def query(self, val: int, l: int, r: int) -> Tuple:
        if self.tree[l].l >= l <= self.tree[r].r <= r:
            return val, self.tree[val].cnt

        mid = self.tree[val].l + self.tree[val].r >> 1
        if l <= mid:
            return self.query(val << 1, l, r)
        if r > mid:
            return self.query(val << 1 | 1, l, r)

class MajorityChecker:

    def __init__(self, arr: List[int]):
        n = len(arr)
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:


if __name__ == '__main__':
    obj = MajorityChecker([1, 1, 2, 2, 1, 1])
    queries = [[0, 5, 4], [0, 3, 3], [2, 3, 2]]
    for l, r, thre in queries:
        print(obj.query(l, r, thre))
