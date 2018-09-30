# -*- coding:utf-8 -*-
# Author: Evan Mi


class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s ...' % (self.name, food))


d = Dog('aix')
d.eat('shit')

lst = [1, 2, 3]
my_dic = {}

try:
    # my_dic['name']
    #lst[20]
    pass
#except KeyError as e:
#    print(e)
#except IndexError as e:
#    print(e)
except (KeyError, IndexError) as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('一切正常')
finally:
    print("不管如何都执行")
