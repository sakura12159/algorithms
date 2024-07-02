# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/29 上午8:55
@Author  : zxy
@File    : 1 无区间更新 区域和检索.py
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


# 单点更新写法
class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.val = 0


class SegmentTree1:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tree = [Node() for _ in range(n << 2)]
        self._build(1, 1, n)

    def _build(self, u, l, r):
        """递归建树"""
        self.tree[u].l = l
        self.tree[u].r = r
        if l == r:
            self.tree[u].val = self.nums[l - 1]
            return

        mid = l + r >> 1
        self._build(u << 1, l, mid)
        self._build(u << 1 | 1, mid + 1, r)
        self._push_up(u)

    def _push_up(self, u):
        """回溯之后更新父节点"""
        self.tree[u].val = self.tree[u << 1].val + self.tree[u << 1 | 1].val

    def update(self, u, x, l, r, k):
        """单点修改值，递归受影响的所有节点"""
        if l == x and r == x:
            self.tree[u].val += k
            return

        mid = l + r >> 1
        if x <= mid:
            self.update(u << 1, x, l, mid, k)
        else:
            self.update(u << 1 | 1, x, mid + 1, r, k)
        self._push_up(u)

    def query(self, u, ql, qr, l, r):
        """区间查询，递归在询问区间内的所有节点"""
        if ql <= l and qr >= r:
            return self.tree[u].val

        mid = l + r >> 1
        s = 0
        if ql <= mid:
            s += self.query(u << 1, ql, qr, l, mid)
        if qr > mid:
            s += self.query(u << 1 | 1, ql, qr, mid + 1, r)
        return s


class NumArray1:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree1(nums)
        self.nums = nums
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(1, index + 1, 1, self.n, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(1, left + 1, right + 1, 1, self.n)


# 区间更新写法
class NodeLz:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.sm = 0
        self.lz = 0  # 懒标记，记录对应值的变化量


class SegmentTree2:
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.tree = [NodeLz() for _ in range(n << 2)]
        self._build(1, 1, n)

    def _push_up(self, u):
        self.tree[u].sm = self.tree[u << 1].sm + self.tree[u << 1 | 1].sm

    def _push_down(self, u):
        """懒更新叶子结点"""
        k = self.tree[u].lz
        self.tree[u << 1].sm += k * (self.tree[u << 1].r - self.tree[u << 1].l + 1)
        self.tree[u << 1].lz += k
        self.tree[u << 1 | 1].sm += k * (self.tree[u << 1 | 1].r - self.tree[u << 1 | 1].l + 1)
        self.tree[u << 1 | 1].lz += k
        self.tree[u].lz = 0

    def _build(self, u, l, r):
        self.tree[u].l = l
        self.tree[u].r = r
        if l == r:
            self.tree[u].sm = self.nums[l - 1]
            return

        mid = l + r >> 1
        self._build(u << 1, l, mid)
        self._build(u << 1 | 1, mid + 1, r)
        self._push_up(u)

    def update(self, u, ql, qr, l, r, k):
        if ql <= l and qr >= r:
            self.tree[u].sm += k * (r - l + 1)
            self.tree[u].lz += k
            return

        if self.tree[u].lz:
            self._push_down(u)

        mid = l + r >> 1
        if ql <= mid:
            self.update(u << 1, ql, qr, l, mid, k)
        if qr > mid:
            self.update(u << 1 | 1, ql, qr, mid + 1, r, k)
        self._push_up(u)

    def query(self, u, ql, qr, l, r):
        if ql <= l and qr >= r:
            return self.tree[u].sm

        if self.tree[u].lz:
            self._push_down(u)

        s = 0
        mid = l + r >> 1
        if ql <= mid:
            s += self.query(u << 1, ql, qr, l, mid)
        if qr > mid:
            s += self.query(u << 1 | 1, ql, qr, mid + 1, r)
        return s


class NumArray2:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tr = SegmentTree2(nums)

    def update(self, index: int, val: int) -> None:
        self.tr.update(1, index + 1, index + 1, 1, self.n, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tr.query(1, left + 1, right + 1, 1, self.n)


# 动态开点 单点修改
class NodeDy1:
    def __init__(self):
        self.ls = 0
        self.rs = 0
        self.v = 0


class SegmentTree3:
    def __init__(self, nums):
        self.idx = 1
        self.tree = defaultdict(NodeDy1)  # 动态开点，可估计点数，也可使用动态指针，对于 py 无区别
        for i, x in enumerate(nums, 1):  # 建树，节点索引从 1 开始
            self.update(1, i, 1, len(nums), x)

    def _push_up(self, u):
        self.tree[u].v = self.tree[self.tree[u].ls].v + self.tree[self.tree[u].rs].v

    def _push_down(self, u):
        """动态开点"""
        if not self.tree[u].ls:
            self.idx += 1
            self.tree[u].ls = self.idx
        if not self.tree[u].rs:
            self.idx += 1
            self.tree[u].rs = self.idx

    def update(self, u, x, ls, rs, k):
        if ls == x and rs == x:
            self.tree[u].v += k
            return

        self._push_down(u)
        mid = ls + rs >> 1
        if x <= mid:
            self.update(self.tree[u].ls, x, ls, mid, k)
        else:
            self.update(self.tree[u].rs, x, mid + 1, rs, k)
        self._push_up(u)

    def query(self, u, ql, qr, l, r):
        if ql <= l and qr >= r:
            return self.tree[u].v

        self._push_down(u)
        s = 0
        mid = l + r >> 1
        if ql <= mid:
            s += self.query(self.tree[u].ls, ql, qr, l, mid)
        if qr > mid:
            s += self.query(self.tree[u].rs, ql, qr, mid + 1, r)
        return s


class NumArray3:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tr = SegmentTree3(nums)

    def update(self, index: int, val: int) -> None:
        self.tr.update(1, index + 1, 1, self.n, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tr.query(1, left + 1, right + 1, 1, self.n)


class NodeDy2:
    def __init__(self):
        self.ls = 0
        self.rs = 0
        self.v = 0
        self.lz = 0


# 动态开点 区间修改
class SegmentTree4:
    def __init__(self, nums):
        self.idx = 1
        self.tree = defaultdict(NodeDy2)
        for i, x in enumerate(nums, 1):
            self.update(1, i, i, 1, len(nums), x)

    def _push_up(self, u):
        self.tree[u].v = self.tree[self.tree[u].ls].v + self.tree[self.tree[u].rs].v

    def _push_down(self, u):
        """动态开点 + 懒标记更新"""
        if not self.tree[u].ls:
            self.idx += 1
            self.tree[u].ls = self.idx
        if not self.tree[u].rs:
            self.idx += 1
            self.tree[u].rs = self.idx

        k = self.tree[u].lz
        if not k:
            return

        self.tree[self.tree[u].ls].lz += k
        self.tree[self.tree[u].rs].lz += k
        self.tree[self.tree[u].ls].v += k
        self.tree[self.tree[u].rs].v += k
        self.tree[u].lz = 0

    def update(self, u, ql, qr, ls, rs, k):
        if ql <= ls and qr >= rs:
            self.tree[u].v += k
            self.tree[u].lz += k
            return

        self._push_down(u)
        mid = ls + rs >> 1
        if ql <= mid:
            self.update(self.tree[u].ls, ql, qr, ls, mid, k)
        if qr > mid:
            self.update(self.tree[u].rs, ql, qr, mid + 1, rs, k)
        self._push_up(u)

    def query(self, u, ql, qr, ls, rs):
        if ql <= ls and qr >= rs:
            return self.tree[u].v

        self._push_down(u)
        s = 0
        mid = ls + rs >> 1
        if ql <= mid:
            s += self.query(self.tree[u].ls, ql, qr, ls, mid)
        if qr > mid:
            s += self.query(self.tree[u].rs, ql, qr, mid + 1, rs)
        return s


class NumArray4:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tr = SegmentTree4(nums)

    def update(self, index: int, val: int) -> None:
        self.tr.update(1, index + 1, index + 1, 1, self.n, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.tr.query(1, left + 1, right + 1, 1, self.n)


if __name__ == '__main__':
    # 单点修改
    obj1 = NumArray1([1, 3, 5])
    print(obj1.sumRange(0, 2))
    obj1.update(1, 2)
    print(obj1.sumRange(0, 2))

    # 区间修改
    obj2 = NumArray2([1, 3, 5])
    print(obj2.sumRange(0, 2))
    obj2.update(1, 2)
    print(obj2.sumRange(0, 2))

    obj3 = NumArray3([1, 3, 5])
    print(obj3.sumRange(0, 2))
    obj3.update(1, 2)
    print(obj3.sumRange(0, 2))

    obj4 = NumArray4([1, 3, 5])
    print(obj4.sumRange(0, 2))
    obj4.update(1, 2)
    print(obj4.sumRange(0, 2))
