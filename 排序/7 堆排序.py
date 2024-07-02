# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/22 下午1:53
@Author  : zxy
@File    : 7 堆排序.py
"""
from mods import *

"""
https://www.runoob.com/w3cnote/heap-sort.html
https://zhuanlan.zhihu.com/p/124885051
堆排序
    1 先将初始的R[0…n-1]建立成最大堆，此时是无序堆，而堆顶是最大元素。
    2 再将堆顶R[0]和无序区的最后一个记录R[n-1]交换，由此得到新的无序区R[0…n-2]和有序区R[n-1]，
    且满足R[0…n-2].keys ≤ R[n-1].key
    3 由于交换后新的根R[1]可能违反堆性质，故应将当前无序区R[1..n-1]调整为堆。
    然后再次将R[1..n-1]中关键字最大的记录R[1]和该区间的最后一个记录R[n-1]交换，
    由此得到新的无序区R[1..n-2]和有序区R[n-1..n]，且仍满足关系R[1..n-2].keys≤R[n-1..n].keys，
    同样要将R[1..n-2]调整为堆。
    4 直到无序区只有一个元素为止。
"""


def heap_sort(arr: List[int]) -> None:
    n = len(arr)

    def swap(i: int, j: int) -> None:
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(root_idx: int, unordered_len: int) -> None:
        """
        调整索引介于 root_idx 至 n 的堆结构
        Args:
            root_idx: 根节点索引
            unordered_len: 未排序的数组长度

        Returns:

        """
        mx = root_idx  # 根节点索引与值
        left, right = (root_idx << 1) + 1, (root_idx << 1) + 2  # 左右节点索引
        if left < unordered_len and arr[left] > arr[mx]:
            mx = left
        if right < unordered_len and arr[right] > arr[mx]:
            mx = right
        if mx != root_idx:
            swap(mx, root_idx)  # 交换根节点与较大叶节点的值
            heapify(mx, unordered_len)

    def build_max_heap() -> None:
        for i in range(n // 2 - 1, -1, -1):  # 从第一个非叶子结点开始将数组堆化
            heapify(i, n - 1)

    build_max_heap()
    # 每次都是移出最顶层的根节点A[0]，与最尾部节点位置调换，同时遍历长度 - 1。
    # 然后从新整理被换到根节点的末尾元素，使其符合堆的特性。
    # 直至未排序的堆长度为0。
    for i in range(n - 1, 0, -1):
        swap(0, i)
        heapify(0, i)


if __name__ == '__main__':
    arr = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    heap_sort(arr)
    print(arr)
