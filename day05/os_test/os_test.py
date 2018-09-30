# -*- coding:utf-8 -*-
# Author: Evan Mi
import os
# 获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())
# 切换当前路径
os.chdir('c:/users')
os.chdir(r'c:\users')
print(os.getcwd())  # 验证当前路径是否切换成功
# 返回当前目录的字符串名 .
print(os.curdir)
# 返回当前目录的父目录的字符串名 ..
print(os.pardir)
# 递归创建各级目录
os.makedirs(r'e:\a\b\c\d')
# 递归删除各级空目录
os.removedirs(r'e:\a\b\c\d')
# 创建一级目录，不能递归创建
os.mkdir(r'e:/test_python')
# 删除一级目录，切该目录不能为空
os.rmdir(r'e:\test_python')
# 以列表的方式列出指定目录的内容
print(os.listdir('.'))
# 删除指定文件
# os.remove(r'e:\test.txt')
# 把test.txt重命名为test1.txt
# os.rename(r'e:\test.txt', r'e:\test1.txt')
# 查看文件的状态信息
print(os.stat(r'e:\test.dcm'))
"""
os.stat_result(st_mode=33206, st_ino=3659174697270772, 
st_dev=505418071, st_nlink=1, st_uid=0, st_gid=0, 
st_size=19468, st_atime=1515546652, st_mtime=1515546652, 
st_ctime=1515546652)
"""
# 当前操作系统的路径分隔符
print(os.sep)
# 当前操作系统的换行符
print(os.linesep)
# 环境变量之间的分隔符
print(os.pathsep)
# 查看系统的环境变量
print(os.environ)
# 查看当前系统的名称
print(os.name)
# 运行shell命令,直接显示结果
# print(os.system('dir'))
# 返回path规范化的绝对路径
print(os.path.abspath(__file__))
# 把路径分割成目录和文件名二元组返回
print(os.path.split(__file__))
# 返回path的目录，其实就是os.path.split(path)的第一个元素
print(os.path.dirname(__file__))
# 返回path的最后的文件名，如果path不是文件则返回空，其实就是os.path.split(path)的第二个元素
print(os.path.basename(__file__))
#  如果path存在，返回True；如果path不存在，返回False
print(os.path.exists(__file__))
# 如果path是绝对路径，返回True
print(os.path.isabs(__file__))
# 如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile(__file__))
# 如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir(__file__))
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join('c:\\', 'a', 'b'))
# 返回path所指向的文件或者目录的最后存取时间
print(os.path.getatime(__file__))
#  返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime(__file__))
