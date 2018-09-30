# -*- coding:utf-8 -*-
# Author: Evan Mi
# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# exchange --> fanout|direct|topic


channel.basic_publish(exchange='logs',
                      routing_key='',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 使消息持久化
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
