import os
import time
import logging


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("{}/logs/{}.log".format(root_path, time.strftime("%Y%m%d", time.localtime())))
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)