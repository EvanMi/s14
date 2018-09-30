# -*- coding:utf-8 -*-
# Author: Evan Mi
from . import module_alex
# 把module_alex模块中的所有内容解析一次，然后赋值给这里的‘module_alex’变量
# from module_alex import *  把模块中的所有内容拿到这里
# from module_alex import say_hello  把模块中的say_hello拿到这里
# from module_alex import say_hello as say_hello_alex 把模块中的say_hello拿到这里,起个名字叫say_hello_alex
# from module_alex import m1, m2, m3 从一个模块中导入多个
# 有了from以后，就不能再使用模块名.方法来调用了
# from 目录 import 模块/包
# from . import 模块/包
# from .. import p_test
# 你运行程序的地方不能在任何的from之后的文件夹/包/模块中
"""
导入模块的本质：
就是把python文件执行一遍

包的本质就是一个目录（必须带有一个__init__.py文件）
包从逻辑上来组织模块，用来存放一堆模块.
导入包的本质，就是执行包中的__init__.py文件
"""

"""
如果在sys.path已经存在了某个包或者模块（python文件）的父目录
那么在运行脚本中直接使用import 模块 就会把模块执行一次，并赋值给变量 ；然后通过模块.方法/属性来调用
直接使用import 包，会调用包中的__init__模块 在__init__中必须用 from . import 模块，把该包下的模块加载进来
然后通过包.模块.方法/属性来调用

如果在sys.path已经存在了某个文件夹、包、或者模块的父目录
那么在运行脚本中使用
from 文件夹 import 模块    -----来引入该文件夹下的模块，并赋值给import后的变量
from 包  import 模块  -----来引入该包下的模块，并赋值给import后的变量
from 模块 import 函数/变量 -----来引入该模块中的方法或者变量

"""

print('----')
