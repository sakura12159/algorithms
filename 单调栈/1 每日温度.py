# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/17 上午10:52
@Author  : zxy
@File    : 1 每日温度.py
"""
from mods import *

"""
https://leetcode.cn/problems/daily-temperatures/
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，
下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
"""


def func(temperatures: List[int]) -> List[int]:
    # 从左到右记录未算出更大元素的数的下标
    # sta = []
    # res = [0] * len(temperatures)
    # for i, x in enumerate(temperatures):
    #     while sta and x > temperatures[sta[-1]]:
    #         j = sta.pop()
    #         res[j] = i - j
    #     sta.append(i)
    # return res

    # 从右到左记录下一个更大元素的候选项
    n = len(temperatures)
    ans = [0] * n
    st = []
    for i in range(n - 1, -1, -1):
        while st and temperatures[i] >= temperatures[st[-1]]:
            st.pop()
        if st:
            ans[i] = st[-1] - i
        st.append(i)
    return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(func(temperatures))
