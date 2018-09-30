# -*- coding:utf-8 -*-
# Author: Evan Mi
import pickle


def say_name(name):
    print('hello %s' % name)


dc = {
    'name': 'alax',
    'age': 12,
    'fun': say_name
}

with open('testp.txt', 'wb') as f:
    f.write(pickle.dumps(dc))

with open('testp.txt', 'rb') as f:
    data = pickle.loads(f.read())
    print(data)
