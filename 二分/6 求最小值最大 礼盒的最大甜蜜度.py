# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/8 上午9:29
@Author  : zxy
@File    : 6 求最小值最大 礼盒的最大甜蜜度.py
"""
from mods import *

"""
https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/
给你一个正整数数组 price ，其中 price[i] 表示第 i 类糖果的价格，另给你一个正整数 k 。
商店组合 k 类 不同 糖果打包成礼盒出售。礼盒的 甜蜜度 是礼盒中任意两种糖果 价格 绝对差的最小值。
返回礼盒的 最大 甜蜜度。
"""


def func(price: List[int], k: int) -> int:
    # 「任意两种糖果价格绝对差的最小值」等价于「排序后，任意两种相邻糖果价格绝对差的最小值」
    price.sort()

    def f(mid):
        """甜蜜度至少为mid时，至多能选多少类糖果"""
        cnt, pre = 1, price[0]
        for p in price:
            if p >= pre + mid:
                cnt += 1
                pre = p
        return cnt

    l, r = 1, (price[-1] - price[0]) // (k - 1)  # 最小值不会超过平均值
    while l <= r:
        mid = (l + r) // 2
        if f(mid) >= k:
            l = mid + 1
        else:
            r = mid - 1
    return r


if __name__ == '__main__':
    price = [13, 5, 1, 8, 21, 2]
    k = 3
    print(func(price, k))
