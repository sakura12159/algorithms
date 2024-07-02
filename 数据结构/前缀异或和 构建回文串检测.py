# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/20 上午9:39
@Author  : zxy
@File    : 前缀异或和 构建回文串检测.py
"""
from mods import *

"""
https://leetcode.cn/problems/can-make-palindrome-from-substring/
给你一个字符串 s，请你对 s 的子串进行检测。
每次检测，待检子串都可以表示为 queries[i] = [left, right, k]。
我们可以 重新排列 子串 s[left], ..., s[right]，并从中选择 最多 k 项替换成任何小写英文字母。 
如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 true，否则结果为 false。
返回答案数组 answer[]，其中 answer[i] 是第 i 个待检子串 queries[i] 的检测结果。
注意：在替换时，子串中的每个字母都必须作为 独立的 项进行计数，也就是说，
如果 s[left..right] = "aaa" 且 k = 2，我们只能替换其中的两个字母。
（另外，任何检测都不会修改原始字符串 s，可以认为每次检测都是独立的）
"""


def func(s: str, queries: List[List[int]]) -> List[bool]:
    # 思路：计算出现奇数次字符的数量，如果 奇数次字符串数量 // 2 <= k，则可以构成回文字符串

    # 前缀和
    # 求字符出现次数的前缀和
    # pre_sum = [[0] * 26]
    # for x in s:
    #     pre_sum.append(pre_sum[-1][:])
    #     pre_sum[-1][ord(x) - 97] += 1
    #
    # ans = []
    # for l, r, k in queries:
    #     cnt = 0  # 出现奇数次的字符种类数
    #     for lc, rc in zip(pre_sum[l], pre_sum[r + 1]):
    #         cnt += (rc - lc) & 1
    #     ans.append(cnt // 2 <= k)
    # return ans

    # 前缀和优化 1，只关注各字符出现次数的奇偶性
    # pre_sum = [[0] * 26]
    # for x in s:
    #     pre_sum.append(pre_sum[-1][:])
    #     pre_sum[-1][ord(x) - 97] = 1 - pre_sum[-1][ord(x) - 97]  # 用0 1表示奇偶次出现次数
    #
    # ans = []
    # for l, r, k in queries:
    #     cnt = 0
    #     for lc, rc in zip(pre_sum[l], pre_sum[r + 1]):
    #         cnt += lc != rc  # 只有1 0与0 1相减时会产生奇数
    #     ans.append(cnt // 2 <= k)
    # return ans

    # 前缀和优化 2，位运算代替减法
    # pre_sum = [[0] * 26]
    # for x in s:
    #     pre_sum.append(pre_sum[-1][:])
    #     pre_sum[-1][ord(x) - 97] ^= 1  # 用0 1表示奇偶次出现次数
    #
    # ans = []
    # for l, r, k in queries:
    #     cnt = 0
    #     for lc, rc in zip(pre_sum[l], pre_sum[r + 1]):
    #         cnt += lc ^ rc
    #     ans.append(cnt // 2 <= k)
    # return ans

    # 前缀异或和
    pre_sum = [0]
    for x in s:
        bit = 1 << (ord(x) - 97)
        pre_sum.append(pre_sum[-1] ^ bit)  # 该比特对应字母的奇偶性：奇数变偶数，偶数变奇数

    ans = []
    for l, r, k in queries:
        cnt = (pre_sum[l] ^ pre_sum[r + 1]).bit_count()
        ans.append(cnt // 2 <= k)
    return ans


if __name__ == '__main__':
    s = "abcda"
    queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
    print(func(s, queries))
