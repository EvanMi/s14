# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello1', durable=True)


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
