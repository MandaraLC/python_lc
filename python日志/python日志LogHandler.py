import time

from data.logHandler import LogHandler

spider_name = "测试log"
logger = LogHandler(spider_name)

for i in range(20):
    logger.info(f'我是提示信息{i+1}')
    logger.error(f'我是错误信息{i+1}')
    time.sleep(1)