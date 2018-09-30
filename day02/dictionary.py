# -*- coding:utf-8 -*-
# Author: Evan Mi

info = {
    'stu1101': 'TengLan Wu',
    'stu1102': 'LongZe Luola',
    'stu1103': 'XiaoZe Maliya'
}  # 字典是无序的
print(info)
print(info['stu1101'])  # 不存在会报错
print(info.get('stu1101'))  # 不存在返回None
print('stu1103' in info)  # 判断是否包含某个key


info['stu1101'] = 'Wu TengLan'  # 存在修改
info['stu1104'] = 'Cang Jin Kong'  # 不存在添加
print(info)
print('split'.center(50, '*'))
# 删除
# del info['stu1101'] #删除字典中key为stu1101的key-value对
# tem = info.pop('stu1102') #返回key所对应的value，并删除字典中的key-value对
# print(tem)
# ite = info.popitem() # 随机删除一个 并以tuple的方式返回 也就是(key,value)
# print(ite)
print('split'.center(50, '*'))
print(info)
print(info.values())  # 和info.keys()都返回一个迭代器对象，用list()方法来转为列表
print(list(info.values())[0])
print(info.keys())
print('split'.center(50, '*'))
print(info.setdefault('stu1101', 'Pig'))  # 如果不存在，设置值并返回，如果存在，不设置值，返回已经存在的值
print(info)
print(info.setdefault('stu1108', 'Pig'))
print(info)
print('split'.center(50, '*'))
b = {
    'stu1101': 'Alex',
    1: 3,
    2: 5
}
info.update(b)  # 用另外一个字典来更新info
print(info)
iite = info.items()  # 也是一个迭代器对象，返回字典中的所有key-value的元组形式的迭代器
# 如果转化为列表，就是[(k1,v1),(k2,v2),(k3,v3)]
print(list(iite)[0][0])

# 给定一组key，然后给定初始值；把所有的key都赋值初始值（default字段）
tem = dict.fromkeys(['stu1101', 5, 6], 'test')  # default字段是浅复制的要注意
print(tem)


for i in info:  # i是info的key
    print(i, info[i])

for k, v in info.items():  # 不高效不建议使用
    print(k, v)
print("hello".center(50, "*"))
for x in info.keys():
    print(x)
