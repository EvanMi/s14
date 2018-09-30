# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 申明queue
channel.queue_declare(queue='hello1', durable=True)
# exchange --> fanout|direct|topic
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 使消息持久化
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
