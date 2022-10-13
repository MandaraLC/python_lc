import time

from redis import Redis

redis_pool = Redis(host='127.0.0.1', port=6379, db=15, password='123456')

#消费者，向列表右侧取出数据，如果没有数据就等待2秒
def consumer():
    while True:
        data = redis_pool.rpop('queue_int')
        if data is None:
            print("等待2秒...")
            time.sleep(2)
            continue
        print(data)
        print("============================================")

if __name__ == "__main__":
    consumer()