# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/7 下午6:48
@Author  : zxy
@File    : 0 边界问题.py
"""
from mods import *


# 查找第一个大于等于目标值的元素索引
def lower_bound_close(nums: List[int], val: int) -> int:
    n = len(nums)
    # [left, right]
    # l, r = 0, n - 1
    # # l 一定指向是，r 一定指向否
    # while l <= r:  # 区间不为空
    #     mid = (l + r) // 2
    #     if nums[mid] >= val:
    #         r = mid - 1  # [left, mid - 1]，因为右闭，需-1
    #     else:
    #         l = mid + 1  # [mid + 1, right]，因为左闭，需+1
    # # 循环结束时 l 等于 r + 1，返回 l 或 r + 1 均可
    # return l

    # (left, right]
    # l, r = -1, n - 1
    # # l + 1 一定指向是，r一定指向否
    # while l < r:
    #     mid = (l + r + 1) // 2
    #     if nums[mid] >= val:
    #         r = mid - 1  # (left, mid - 1]，因为右闭，需-1
    #     else:
    #         l = mid  # (mid, right]，因左开，不用动
    # # 循环结束时 l 等于 r，返回 l + 1 或 r + 1 均可
    # return l + 1

    # [left, right)
    # l, r = 0, n
    # # l 一定指向是，r - 1 一定指向否
    # while l < r:
    #     mid = (l + r) // 2
    #     if nums[mid] >= val:
    #         r = mid  # [left, mid)，右开不用动
    #     else:
    #         l = mid + 1  # [mid + 1, right)，左闭，需+1
    # # 循环结束时 l 等于 r，返回 l 或 r 均可
    # return l

    # (left, right)
    l, r = -1, n
    # l + 1一定指向是，r - 1 一定指向否
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] >= val:
            r = mid  # (left, mid)，左开不用动
        else:
            l = mid  # (mid, right)，右开，不用动
    # 循环结束时 l + 1 等于 r，返回 l + 1 或 r 均可
    return r


# 查找第一个大于目标值的元素索引
def lower_bound_open(nums: List[int], val: int) -> int:
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 4, 5, 5, 6]
    val = 4
    print(f"{nums = }, {val = }")
    # 第一个大于等于 val 的索引
    print(lower_bound_close(nums, val))
    # 第一个大于 val 的索引
    print(lower_bound_open(nums, val))
    # 最后一个小于等于 val 的索引 = 第一个大于 val 的索引 - 1
    print(lower_bound_open(nums, val) - 1)
    # 最后一个小于 val 的索引 = 第一个大于等于 val 的索引 - 1
    print(lower_bound_close(nums, val) - 1)
