# -*- coding:utf-8 -*-
# Author: Evan Mi

"""
data = open("E:/pythondata/day02/yesterday.txt").read()
print(data)
"""
# r是读模式，找不到文件会报错  r+ 在读的基础上有了写的能力，这里的写就是追加
# w是写模式,会创建一个文件，存在也会直接覆盖  w+ 写的过程中，可以读，这里的写是一直在文件尾追加
# a追加模式，存在的时候追加，不存在的时候创建 a+ 追加的过程中，可以读
f = open("E:/pythondata/day02/yesterday.txt", 'r+')  # 句柄 也就是文件的内存对象
f2 = open('E:/pythondata/day02/yesterday2.txt', 'w')
# f = open("E:/pythondata/day02/yesterday.txt", 'rb') # 以二进制读取文件内容
# f = open("E:/pythondata/day02/yesterday.txt", 'wb') # 向文件中写入二进制
"""
data = f.read()     # 一次读完文件的所有内容，光标指向了文件的末尾之后
data2 = f.read()    # 再读就没有了
print(data)
print("ss".center(20, '#'))
print(data2)
f.write('i love beijing\n')
f.write('what \n')
"""
# 返回一个以行为元素的列表
# f.readlines()
# 读一行 光标指向下一行
# print(f.readline())
# for i in range(5):
#    print(f.readline())

#  只适合处理小文件
"""
for index, line in enumerate(f.readlines()):
    if index == 9:
        print('line 9'.center(50, '-'))
    else:
        print(line.strip())
"""

"""
# 节省内存的高效按行读取文件，使用迭代器，读一行加载一行，读过的行就不在内存中了
count = 0
for line in f:
    count += 1
    if count == 10:
        print('line 9'.center(50, '-'))
    else:
        print(line.strip())
"""
"""
# 返回当前光标位置（第几个字符）
print(f.tell())
# 读指定长度个字符
print(f.read(50))
print(f.tell())
# 光标指向第n个字符
f.seek(10)
print(f.readline())
"""
"""
# 打印文件的字符编码
print(f.encoding)
"""
# 文件句柄的编号
# print(f.fileno())
# 是否能移动
# print(f.seekable())
# 是否可读
# print(f.readable())
# 是否可写
# print(f.writable())
# 文件名
# print(f.name)
# 强制刷写缓存区
# f.flush()
# 文件是否关闭
# f.closed
# 截断文件到指定长度，不指定长度，就会截断为0
# f.truncate(50)


"""
文件的修改 写到新文件中，然后删除旧文件，把新文件的名字改成旧文件
"""
for line in f:
    if line.strip() == 'In years gone by， 岁月如何消逝':
        f2.write('hhhhhsdsd\n')
    else:
        f2.write(line)

f2.flush()
# 关闭文件句柄
f.close()
f2.close()
