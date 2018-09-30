# -*- coding:utf-8 -*-
# Author: Evan Mi
import shutil
"""
主要作用是拷贝文件、拷贝文件的权限、状态信息以及压缩文件、移动文件、删除文件
"""

# 将一个文件对象的内容拷贝到另一个文件对象中,可以部分内容
"""
f1 = open(r'E:\pythondata\day05\test.txt', 'rb')
f2 = open(r'E:\pythondata\day05\test1.txt', 'wb')
shutil.copyfileobj(f1, f2)
shutil.copyfileobj(f1, f2, 29) #部分拷贝
"""
# 不用创建文件对象，直接用文件的路径实现文件的拷贝
"""
shutil.copyfile(r'E:\pythondata\day05\test.txt', r'E:\pythondata\day05\test1.txt')
"""
# 将源文件的权限信息拷贝到目标文件
"""
shutil.copymode(r'E:\pythondata\day05\test.txt', r'E:\pythondata\day05\test1.txt')
"""
# 将源文件的所有状态信息都拷贝到目标文件
"""
shutil.copystat(r'E:\pythondata\day05\test.txt', r'E:\pythondata\day05\test1.txt')
"""
# 同时拷贝文件内容和权限
"""
shutil.copy(r'E:\pythondata\day05\test.txt', r'E:\pythondata\day05\test1.txt')
"""
# 同时拷贝文件内容和所有的状态信息
"""
shutil.copy2(r'E:\pythondata\day05\test.txt', r'E:\pythondata\day05\test1.txt')
"""
# 拷贝目录下所有的内容到新的目录下，递归方式的拷贝
"""
shutil.copytree(r"e:\test", r"e:\test2")
"""
# 删除目录并清空下面的所有内容
"""
shutil.rmtree(r'e:\test2')
"""
# 移动文件夹即下面的内容到新的文件夹中
"""
shutil.move(r'e:\test', r'e:\test2')
"""
# 将指定的文件夹压缩  zip|tar|bztar|gztar
"""
ret = shutil.make_archive(r'E:\pythondata\day05\wwwwwwww', 'gztar', root_dir=r'E:\pythondata\day05')
"""


