import time

from redis import Redis

redis_pool = Redis(host='127.0.0.1', port=6379, db=15, password='123456')

#每隔一秒向队列左侧插入数据
def produce():
    for i in range(20):
        redis_pool.lpush("queue_int", i+1)
        time.sleep(1)

if __name__ == '__main__':
    produce()