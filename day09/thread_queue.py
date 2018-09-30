# -*- coding:utf-8 -*-
# Author: Evan Mi
import queue

q = queue.Queue()
# 后进先出的队列
# q = queue.LifoQueue()
# 设置队列的大小
# q = queue.Queue(maxsize=20)
# 满了的时候阻塞
q.put('d1')
q.put('d2')
q.put('d2')
# 满了的时候会抛出异常
# 满了的时候会抛出异常
# q.put_nowait('dd')
print('size', q.qsize())

# 队列为空的时候阻塞
val = q.get()
q.task_done()  # 在get之后通过调用task_done()来使得队列中的总元素个数减一，用来触犯q.join()方法
print(val)
val = q.get()
q.task_done()
print(val)
val = q.get()
q.task_done()
print(val)
print('size:', q.qsize())
# 设置超时时间
# q.get(timeout=10)
# 空的时候会抛出异常，通过捕获异常来处理队列为空
# q.get_nowait()
q.join()  # 会被阻塞在这里，直到
print("finish")
"""
print("split".center(200, '*'))
pq = queue.PriorityQueue()
pq.put((10, 'alex'))
pq.put((100, 'evan'))
pq.put((-3, 'xx'))
pq.put((5, 'aex'))
pq.put((2, 'lex'))
"""