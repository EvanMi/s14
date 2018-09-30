# -*- coding:utf-8 -*-
# Author: Evan Mi
import threading
import time

num = 0
# 同一个线程只能acquire一次，再acquire的话就会阻塞，造成死锁
lock = threading.Lock()
# 同一个线程可以一直acquire,但是每次acquire之后必须有release
# threading.RLock()
# 定义信号量
# semaphore = threading.BoundedSemaphore(5)   # 最多同时有五个线程访问
# semaphore.acquire()
# semaphore.release()


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n

    def run(self):
        lock.acquire()
        global num
        num += 1
        lock.release()
        print('running task ', self.n)
        time.sleep(2)
        print(self.n, 'done')


star_time = time.time()

for i in range(50):
    mt = MyThread(i)
    #  把当前线程设置为守护线程
    #  mt.setDaemon(True)
    mt.start()

end_time = time.time()
print(end_time-star_time)
print(threading.current_thread(), threading.active_count())
time.sleep(15)
print('num:', num)
