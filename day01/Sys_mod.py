# -*- coding:utf-8 -*-
# Author: Evan Mi
#  import sys

#  print(sys.path)  # 打印环境变量
#  print(sys.argv)  # 取参数

import os  # 用来与系统交互

# cmd_res = os.system("dir")  # 执行系统命令

# print("-->", cmd_res)  #cmd_res只代表了命令的执行是否成功，返回结果不会给它，而是直接打印到屏幕上

cmd_res_s = os.popen("dir").read()
print("-->", cmd_res_s)
# os.mkdir("new_dir")

"""
'C:\\Users\\user\\PycharmProjects\\s14\\day01',
'C:\\Users\\user\\PycharmProjects\\s14', 
'C:\\Users\\user\\PycharmProjects\\s14\\venv\\Scripts\\python35.zip',
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35\\DLLs', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35\\lib', 
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python35',
'C:\\Users\\user\\PycharmProjects\\s14\\venv',
'C:\\Users\\user\\PycharmProjects\\s14\\venv\\lib\\site-packages',    第三方库保存在这里
'C:\\Users\\user\\PycharmProjects\\s14\\venv\\lib\\site-packages\\setuptools-28.8.0-py3.5.egg',
'C:\\Users\\user\\PycharmProjects\\s14\\venv\\lib\\site-packages\\pip-9.0.1-py3.5.egg',
'D:\\新建文件夹\\PyCharm 2017.3\\helpers\\pycharm_matplotlib_backend'
"""


"""
在python3中已经没有了长整型一说，所有的整数都是整型
"""

"""三元运算"""
a, b, c = 1, 3, 5
d = a if a > b else c

byval = "我们是一个好好好?".encode('utf-8')
print(byval)
print(byval.decode('utf-8'))
