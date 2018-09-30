# -*- coding:utf-8 -*-
# Author: Evan Mi

# class People  经典类


class Relation(object):

    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))


class People(object):       # 新式类  多继承和经典类不同

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating .." % self.name)

    def sleep(self):
        print("%s is sleeping .." % self.name)

    def talk(self):
        print("%s is talking .." % self.name)

    def run(self):
        print("running %s" % self.name)

    def __help(self):
        print("helping someone %s" % self.name)


class Man(Relation, People):

    def __init__(self, name, age, money):
        #  People.__init__(self, name, age)  经典类的写法
        print(super(Man, self))
        super(Man, self).__init__(name, age)  # 新式类的写法
        self.money = money

    def piao(self):
        print("%s is piaoing ... 20s ... done" % self.name)

    def sleep(self):
        print("man is sleeping")

    def talk(self):
        # People.eat(self)  # 调用父类的eat方法
        super(Man, self).eat()
        print('man is eating')


class Woman(People, Relation):
    def get_birth(self):
        print("%s is born a baby" % self.name)

    def talk(self, language):   # 覆盖父类的方法，即便是参数的个数、类型不同
        print('%s is talking %s' % (self.name, language))


m1 = Man("alax", 12, 22)
#m1.eat()
#m1.piao()
#m1.sleep()
m1.talk()

w1 = Woman('chn', 22)
#w1.get_birth()

# m1.make_friends(w1)
