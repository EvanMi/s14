# -*- coding:utf-8 -*-
# Author: Evan Mi
from redishelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)
