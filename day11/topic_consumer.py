# -*- coding:utf-8 -*-
# Author: Evan Mi
# -*- coding:utf-8 -*-
# Author: Evan Mi
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    # sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    # sys.exit()
    binding_keys = ['info', 'warning', 'error']

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)


def callback(ch, method, properties, body):
    print("[x] Received %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
