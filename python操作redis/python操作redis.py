import redis

redis_pool = redis.Redis(host='127.0.0.1', port=6379, password='123456', db=0)
redis_pool.set("username", "nihao")

getusername = redis_pool.get("username")
print(getusername)