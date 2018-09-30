# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True) # 不需要指定queue名字
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
