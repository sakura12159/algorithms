# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/21 下午5:27
@Author  : zxy
@File    : 链表归并排序.py
"""
from mods import *

"""
https://leetcode.cn/problems/sort-list/
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(nodes: List) -> Optional[ListNode]:
    ans = dummy = ListNode(-1)
    for x in nodes:
        dummy.next = ListNode(x)
        dummy = dummy.next
    return ans.next


def visualize(head: Optional[ListNode]) -> List:
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans


def func(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None  # 切割中点

    left, right = func(head), func(mid)
    head = res = ListNode(-1)
    while left and right:
        if left.val < right.val:
            head.next = left
            left = left.next
        else:
            head.next = right
            right = right.next
        head = head.next
    head.next = left if left else right
    return res.next


if __name__ == '__main__':
    nodes = [4, 2, 1, 3, 5, 8, 9, 6]
    head = build(nodes)
    head = func(head)
    print(visualize(head))
