# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/21 下午3:37
@Author  : zxy
@File    : 双向链表 LRU(least recently used)Cache.py
"""
from mods import *

"""
https://leetcode.cn/problems/lru-cache/
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""


class Node:
    __slots__ = 'prev', 'next', 'key', 'val'  # 加快访问速度，节省内存

    def __init__(self, key: int = 0, val: int = -1):
        self.key = key  # 末节点的 key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.hs = {}
        self.capacity = capacity
        self.sent = Node()  # 哨兵节点
        self.sent.prev = self.sent
        self.sent.next = self.sent

    def _push(self, x: Node) -> None:
        """
        添加到哨兵节点后
        Args:
            x: 要添加的节点

        Returns:

        """
        x.prev = self.sent
        x.next = self.sent.next
        x.prev.next = x
        x.next.prev = x

    def _remove(self, x: Node) -> None:
        """
        删除一个节点
        Args:
            x: 要删除的节点

        Returns:

        """
        x.prev.next = x.next
        x.next.prev = x.prev

    def _get(self, key: int) -> Optional[Node]:
        """
        尝试取得一个节点
        Args:
            key: 想取得的节点的 key

        Returns:

        """
        if key not in self.hs:
            return
        node = self.hs[key]
        self._remove(node)
        self._push(node)
        return node

    def get(self, key: int) -> int:
        node = self._get(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self._get(key)
        if node:
            node.val = value
            return
        self.hs[key] = node = Node(key, value)
        self._push(node)
        if len(self.hs) > self.capacity:
            bot_node = self.sent.prev
            del self.hs[bot_node.key]
            self._remove(bot_node)


if __name__ == '__main__':
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    obj = LRUCache(*params[0])
    res = []
    for i in range(1, len(ops)):
        res.append(eval(f"obj.{ops[i]}(*{params[i]})"))
    print(res)
