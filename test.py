# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/5 上午10:18
@Author  : zxy
@File    : test.py
"""

nums = input().split(' ')
for x in nums:
    x = (8 - len(x)) * ' ' + x
print(' '.join(nums))
