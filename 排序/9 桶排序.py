# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 下午3:55
@Author  : zxy
@File    : 9 桶排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/bucket-sort.html
桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
为了使桶排序更加高效，我们需要做到这两点：
    1 在额外空间充足的情况下，尽量增大桶的数量
    2 使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。
"""


def bucket_sort(arr: List[int]) -> List[int]:
    mn, mx = min(arr), max(arr)
    lower, upper = mn // 10, mx // 10 + 1
    buckets = {i: [] for i in range(lower, upper)}  # 映射关系：以 // 10 的结果作为分桶依据
    for x in arr:
        buckets[x // 10].append(x)  # 将各元素分到各自的桶里

    res = []
    for x in range(lower, upper):
        res += sorted(buckets[x])  # 桶内的排序方法
    return res


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    arr = bucket_sort(arr)
    print(arr)
