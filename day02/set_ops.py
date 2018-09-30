# -*- coding:utf-8 -*-
# Author: Evan Mi

# 创建一个set
list_1 = [1, 3, 5, 7, 3, 6, 7, 9]
list_1 = set(list_1)
list_2 = set([2, 6, 0, 66, 22, 8, 4])
print(list_1, type(list_1))


# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集
print(list_1.union(list_2))
print(list_1 | list_2)
# 差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))
print(list_1 - list_2)
list_3 = set([1, 3, 7])
# 判断是否为子集
print(list_3.issubset(list_1))
# 判断是否为父集
print(list_1.issuperset(list_3))
# 对称差 A并B - A交B
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)
# 判断两个集合是否没有交集
print(list_1.isdisjoint(list_2))

# 添加
list_1.add(999)
# 添加多个
list_1.update([888, 777, 555])
# 删除 如果要删除的不存在会报错
list_1.remove(777)
# 删除，如果删除不存在的元素不会报错
list_1.discard(999)
#  随机删除并返回一个值
list_1.pop()
# 长度
print(len(list_1))
# 判断set中是否包含某个元素
print(999 in list_1)




"""
xv = ["" for i in range(10)]
vv = [-1] * 10
print(xv)
print(vv)
"""