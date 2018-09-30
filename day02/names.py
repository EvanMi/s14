# -*- coding:utf-8 -*-
# Author: Evan Mi
import copy

names = ["ZhangYang", "Guyun", "XiangPeng", "XuliangChen"] #创建一个列表
names.append("LeiHaiDong") # 给列表的末尾追加元素
names.insert(1, "ChenRongHua")  # 在指定位置插入元素
names.insert(3, "XinZhiYu")
names[2] = "XieDi"  # 修改指定位置的元素


print(names)  # 打印列表中的全部元素
print(names[0])     # 获得列表中指定位置的元素
print(names[1:3])  # 获得列表中指定范围的元素列表，前闭后开 [start,end)
print(names[-3:-1])  # 获取列表中指定范围的元素列表，负号表示倒数，前闭后开；这里获取倒数第3和倒数第2个数
print(names[-2:])  # 截取倒数第2个元素到列表结束的所有元素
print(names[0:3])  # 截取[0,3)的元素
print(names[:3])    # 截取[列表开头,3)的元素
print(names[::2])  # 指定切分的步长,这里开始和结尾都没有写，就是从整个列表中，每隔2个元素取到新的列表中

# Delete
pop_val = names.pop()  # 默认删除最后一个元素并返回
pop_val_1 = names.pop(0)  # 删除指定位置的元素并返回
names.remove("ChenRongHua")  # 删除某个元素，直接指定元素内容
del names[1]  # 删除指定位置的元素

print(names)
print(names.index("XieDi"))  # 根据元素内容查找元素在列表中的位置
print(names[names.index("XieDi")])


# 统计
print("Count:", names.count("XieDi"))  # 统计列表中指定元素的个数

# 反转
names.reverse()
print(names)
# 排序
names.sort()
print(names)
# 合并其他列表
name_other = ["zhang", "qiu"]
names.extend(name_other)
del name_other

# 清空
names.clear()




print("--------------------------------------------------------------------------------------------------------")
names = ["ZhangYang", "Guyun", "XiangPeng", ["alex", "jack"], "XuliangChen"]
copy_names = names.copy()
copy_names = names[:] #也是浅复制
copy_names = list(names) #也是浅复制
names3 = copy.deepcopy(names)  # 深度复制
print(names)
print(copy_names)
names[2] = "what"
names[3][0] = "evan"
copy_names[2] = "you"
print(names)
print(copy_names)
print(names3)


names = ["ZhangYang", "Guyun", "XiangPeng", ["alex", "jack"], "XuliangChen"]
#遍历
for i in names:
    print(i)


