import uuid
import time
from collections import namedtuple
from redis.exceptions import RedisError

Lock = namedtuple("Lock", ("validity", "resource", "key"))


# class CannotObtainLock(Exception):
#     pass


class MultipleRedlockException(Exception):
    def __init__(self, errors, *args, **kwargs):
        super(MultipleRedlockException, self).__init__(*args, **kwargs)
        self.errors = errors

    def __str__(self):
        return ' :: '.join([str(e) for e in self.errors])

    def __repr__(self):
        return self.__str__()


class Redlock(object):
    default_retry_count = 10
    default_retry_delay = 0.4
    clock_drift_factor = 0.01
    unlock_script = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end"""

    def __init__(self, redis, retry_count=None, retry_delay=None):
        self.redis = redis
        self.retry_count = retry_count or self.default_retry_count
        self.retry_delay = retry_delay or self.default_retry_delay
        self.quorum = (1 // 2) + 1

    def lock_instance(self, resource, val, ttl):
        try:
            assert isinstance(ttl, int), 'ttl {} is not an integer'.format(ttl)
        except AssertionError as e:
            raise ValueError(str(e))
        return self.redis.set(resource, val, nx=True, px=ttl)

    def unlock_instance(self, resource, val):
        try:
            self.redis.eval(self.unlock_script, 1, resource, val)
        except Exception as e:
            pass

    def lock(self, resource, ttl=10000):
        retry = 0
        val = str(uuid.uuid4())

        # Add 2 milliseconds to the drift to account for Redis expires
        # precision, which is 1 millisecond, plus 1 millisecond min
        # drift for small TTLs.
        drift = int(ttl * self.clock_drift_factor) + 2

        redis_errors = list()
        while retry < self.retry_count:
            n = 0
            start_time = int(time.time() * 1000)
            del redis_errors[:]

            try:
                lock_instance = self.lock_instance(resource, val, ttl)
                print('lock_instance:{}'.format(lock_instance))
                if lock_instance:
                    n += 1
            except RedisError as e:
                redis_errors.append(e)

            elapsed_time = int(time.time() * 1000) - start_time
            validity = int(ttl - elapsed_time - drift)
            if validity > 0 and n >= self.quorum:
                if redis_errors:
                    raise MultipleRedlockException(redis_errors)
                return Lock(validity, resource, val)
            else:
                print('加锁失败 validity:{} ,n:{}'.format(validity,n))
                try:
                    self.unlock_instance(resource, val)
                except:
                    pass
                retry += 1
                time.sleep(self.retry_delay)
        return False

    def unlock(self, lock):
        redis_errors = []

        try:
            self.unlock_instance(lock.resource, lock.key)
        except RedisError as e:
            redis_errors.append(e)

        if redis_errors:
            raise MultipleRedlockException(redis_errors)