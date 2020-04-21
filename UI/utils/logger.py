# _*_ coding: utf-8 _*_
import logging
import os.path
import sys
import time

from utils.basepath_helper import logs_path


class Logger(object):
    def __init__(self, name):
        """
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 获取文件所在的目录

        foldername = time.strftime('%Y%m%d', time.localtime(time.time()))        # 获取当前日期，创建一个当前日期的文件夹
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))            # 文件名

        log_path = logs_path + foldername        # 文件地址

        if not os.path.exists(log_path):            # 判断目录是否存在，不存在创建
            os.makedirs(log_path)

        log_name = log_path + '/' + rq + '.log'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式

        formatter = logging.Formatter('%(asctime)s|%(filename)s[line:%(lineno)d] %(levelname)s:%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


# create a logger instance
logger = Logger(name="BasePage").getlog()
