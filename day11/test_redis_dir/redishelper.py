# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis


class RedisHelper(object):

    def __init__(self):
        self.__conn = redis.Redis(host='localhost')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()  # 准备接收
        return pub


if __name__ == '__main__':
    p = RedisHelper()
    p.publish('hell01')
