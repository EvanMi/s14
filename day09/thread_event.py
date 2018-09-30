# -*- coding:utf-8 -*-
# Author: Evan Mi
import threading
import time
# Event 类似java中的synchronized中的signal和wait
event = threading.Event()
event.is_set()

def ligther():
    count = 0
    event.set()
    while True:
        if 20 < count < 30:
            if event.is_set():
                event.clear()
            print('red')
        elif count > 30:
            if not event.is_set():
                event.set()
            count = 0
        else:
            print('green')
        time.sleep(1)
        count += 1


def car(name):
    while True:
        event.wait()
        print('car name # %s # is running' % name)
        time.sleep(2)

light = threading.Thread(target=ligther)
light.start()
car = threading.Thread(target=car, args=('car1',))
car.start()
