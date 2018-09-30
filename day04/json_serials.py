# -*- coding:utf-8 -*-
# Author: Evan Mi
import json


def say_name(name):
    print('hello %s,%s' % (name, name))


info = {
    'name': 'alex',
    'age': 22,
}

say_name('yes')

with open('test.txt', 'w') as f:
    f.write(json.dumps(info))

