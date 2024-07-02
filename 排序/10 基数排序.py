# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 下午4:10
@Author  : zxy
@File    : 10 基数排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/radix-sort.html
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
"""


def radix_sort(arr: List[int]) -> List[int]:
    res = []
    mx_digits = len(str(abs(max(arr))))  # 获取最大的位数

    dev = 1  # 第几位数，个位数为1，十位数为10···
    mod = 10  # 基数
    for _ in range(mx_digits):
        radix = [[] for _ in range(mod * 2)]  # 考虑到负数，我们用两倍队列
        for x in arr:
            radix[x % mod].append(x)  # 将每个元素根据当前数位大小放进不同的桶中
        dev *= 10
        mod *= 10

        res = []
        for x in radix:
            res += x

    return res


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    arr = radix_sort(arr)
    print(arr)
