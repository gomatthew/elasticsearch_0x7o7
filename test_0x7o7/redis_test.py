# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='127.0.0.1', port=6379,decode_responses=True)
r.lpush('test', *[1,2,3])
print(r.lrange('test',0,-1))
res = r.lpop('test')
print(res)
