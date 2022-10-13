import logging

LOG = logging.getLogger()
fh = logging.FileHandler("./log/access.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)  # 把formater绑定到fh上
LOG.addHandler(fh)
LOG.warning("我是日志信息")