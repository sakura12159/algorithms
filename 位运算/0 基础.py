# -*- coding: utf-8 -*-
"""
@Time    : 2024/5/27 下午5:30
@Author  : zxy
@File    : 0 基础.py
"""

# '111111' 表示 {0, 1, 2, 3, 4, 5}，每一个二进制位代表该元素是否存在
a = '001101'  # {0, 2, 3}
b = '110110'  # {1, 2, 4, 5}

a, b = int(a, 2), int(b, 2)
# 交集
print(bin(a & b))  # 0b100: {2}
# 并集
print(bin(a | b))  # 0b111111: {0, 1, 2, 3, 4, 5}
# 对称差，即在两个集合中只出现一次的元素
print(bin(a ^ b))  # 0b111011: {0, 1, 3, 4, 5}
# a 对 b 的差集
print(bin(a & ~ b))  # 0b1001: {0, 3}
# 判断 a 是否为 b 的子集
print(a & b == a)
print(a | b == b)

# 单个元素集合
print(bin(1 << 4))  # 0b10000: {4}
# 全集
print(bin((1 << 6) - 1))  # 0b111111: {0, 1, 2, 3, 4, 5}
# 补集，a 的补集
print(bin(((1 << 6) - 1) ^ a))  # 0b110010: {1, 4, 5}
# 属于，判断 2 是否为 a 的元素
print((a >> 2) & 1 == 1)  # True
# 不属于，判断 1 是否为 a 的元素
print((a >> 1) & 1 == 1)  # False
# 向集合中添加元素，向 a 中添加元素 4
print(bin(a | (1 << 4)))  # 0b11101: {0, 2, 3, 4}
# 从集合中删除元素 3
print(bin(a & ~ (1 << 3)))  # 0b101: {0, 2}
# 从集合中删除一定存在的元素，从 a 中删除 3
print(bin(a ^ (1 << 3)))  # 0b101: {0, 2}
# 删除 a 最小元素，即低二进制位归零
print(bin(a & (a - 1)))  # 0b1100: {2, 3}

# 获得集合大小，即二进制中 1 的个数
print(a.bit_count())  # 3
# 获得集合最大元素
print(a.bit_length() - 1)  # 3
# 获得集合最小元素
print((a & -a) - 1)  # 0

# 遍历集合判断某元素是否在 a 中
for i in range(6):
    if (a >> i) & 1:
        print(f'{i} is in a')

# 枚举所有集合
for i in range(1 << 6):
    cur = set()
    cnt = 0
    for x in bin(i)[2:][::-1]:
        if x == '1':
            cur.add(cnt)
        cnt += 1
    print(f'one set is {cur}')

# 枚举 a 的子集
sub = a
while sub:
    sub = (sub - 1) & a
    cur = set()
    cnt = 0
    for x in bin(sub)[2:][::-1]:
        if x == '1':
            cur.add(cnt)
        cnt += 1
    print(f'one subset of a is {cur}')
