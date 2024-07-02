# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 上午10:18
@Author  : zxy
@File    : 7 求第K小 有序矩阵中第K小的元素.py
"""
from mods import *

"""
https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/
给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
"""


def func(matrix: List[List[int]], k: int) -> int:
    m, n = len(matrix), len(matrix[0])

    # 1 每行查找
    # def f(i, target):
    #     """每一行中查找最后一个小于等于target的数量"""
    #     l, r = 0, n - 1
    #     while l <= r:
    #         mid = l + (r - l) // 2
    #         if matrix[i][mid] > target:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return l
    #
    # l, r = matrix[0][0], matrix[-1][-1]
    # # 搜索第k小的数，即第一个前面有大于等于k的数的值
    # while l <= r:
    #     mid = l + (r - l) // 2
    #     cnt = 0
    #     for i in range(m):
    #         cnt += f(i, mid)
    #     if cnt >= k:
    #         r = mid - 1
    #     else:
    #         l = mid + 1
    # return l

    # 2 列方向二分
    n = len(matrix)

    def check(mid):  # 判断mid是否是第k小的元素
        """遍历获取较小元素部分元素总数，并与k值比较"""
        i, j = n - 1, 0
        num = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                # 当前元素小于mid，则此元素及上方元素均小于mid
                num += i + 1
                # 向右移动
                j += 1
            else:
                # 当前元素大于mid，则向上移动，直到找到比mid小的值，或者出矩阵
                i -= 1
        return num < k

    left, right = matrix[0][0], matrix[-1][-1]
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(func(matrix, k))
