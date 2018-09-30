# -*- coding:utf-8 -*-
# Author: Evan Mi
import time


def auth(auth_type):

    def outer_wrapper(func):
        print(auth_type)

        def wrapper(*args, **kwargs):
            user_name = input('UserName:').strip()
            pass_word = input('passWord:').strip()
            if user_name == 'alax' and pass_word == '123':
                print('User has passed authentication')
                # args ('alaa', 'bbb', 'ccc')
                # kwargs {'age3': 55, 'age': 123, 'age1': 33}
                # 这里用*agrs,**kwargs是指用args中的内容作为func的位置参数，kwargs的内容作为func的键值参数
                return func(*args, **kwargs)
            else:
                exit('Invalid User or Pass')
        return wrapper
    return outer_wrapper


def index():
    print('welcome to index page')


@auth(auth_type="local")
def home():
    print('welcome to home page')
    return 'from home'


@auth(auth_type="remote")
def bbs(name,name1,name2, age,age1,age3):
    print('welcome to bbs page',name,age)


index()
print(home())
bbs('alaa', 'bbb', 'ccc', age=123,age1=33,age3=55)
