# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

serverities = sys.argv[1:]
if not serverities:
    # sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    # sys.exit()
    serverities = ['info', 'warning', 'error']

for serverity in serverities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=serverity)

def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
