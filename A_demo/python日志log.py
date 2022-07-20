from data.logHandler import LogHandler

spider_name = "测试log"
logger = LogHandler(spider_name)

logger.info(u'我是提示信息')

logger.error(u'我是错误信息')