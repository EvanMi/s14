# -*- coding:utf-8 -*-
# Author: Evan Mi
import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool=pool, db=12)
r.set('poolFool', 'poolBar')
print(r.get('poolFool').decode())

pipe = r.pipeline()
pipe.set('name', 'alex')
pipe.set('age', 12)
pipe.execute()

print(r.get('name'))