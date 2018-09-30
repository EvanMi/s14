# -*- coding:utf-8 -*-
# Author: Evan Mi

school = 'hello'

names = ['1', '2', '3']
name7 = 'sss'
name ='alex li'

def change_name(name_a):
    global school, name2  # 永远不要这样用
   # school = 'erbao'  # 没有global的时候，这个school和外面的school不一样
    name2 = "333"
    """
    和外部变量同名，也是两回事，没有任何影响
    前面加上golbal school才能修改外部变量
    """
    """
    在方法中默认可以访问到外层的全局变量，
    但是一但定义了和外部的全局变量同名的变量，
    或者在形参中定义了和外部全局变量同名的变量
    外层的全局变量就不可见了
    """
    print(names)
    print("before change %s" % name_a)
    # name = "Alex Li"
    print("after change %s" % name)
    print(school)
    print(name7)



change_name(name)
print(name)
print(school)
print(name2)
