#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：log.py
"""
import inspect
import traceback
import os
import time
import logging

'''
该日志类可以把不同级别的日志输出到不同的日志文件中
'''
pa = os.path.dirname(__file__)[:-6].replace("\\", "/")
handlers = {
    # logging.NOTSET: "../Log/my_notset.log",
    logging.DEBUG: f"{pa}Log/my_debug.log",
    logging.INFO: f"{pa}Log/my_info.log",
    logging.WARNING: f"{pa}Log/my_warning.log",
    logging.ERROR: f"{pa}Log/my_error.log",
    logging.CRITICAL: f"{pa}Log/my_critical.log"
}


def create_handlers():
    log_levels = handlers.keys()
    for level in log_levels:
        path = os.path.abspath(handlers[level])
        handlers[level] = logging.FileHandler(path)


# 加载模块时创建全局变量
create_handlers()


class MyLog(object):

    def print_now(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self):
        self.__loggers = {}
        log_levels = handlers.keys()
        for level in log_levels:
            logger = logging.getLogger(str(level))
            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def get_log_message(self, level, message):
        frame, filename, lineno, funcName, code, unknowField = inspect.stack()[2]
        '''日志格式：[类型] [时间] [记录代码(文件名，行数)] 信息'''
        return "%s [%s] [%s - %s - %s] \n%s" % (self.print_now(), level, filename, lineno, funcName, message)

    def info(self, message):
        message = self.get_log_message("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.get_log_message("error", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.get_log_message("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.get_log_message("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.get_log_message("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)


logger = MyLog()


if __name__ == "__main__":
    # logger = MyLog()
    # data = "哈哈哈"
    # url = "http://www.baidu.com"
    # logger.debug(f"内容：{data}，请求地址：{url}\n")
    #
    # def open_file():
    #     try:
    #         with open("./12.txt", "r") as f:
    #             f.read()
    #     except FileNotFoundError:
    #         traceback.print_exc()
    #         logger.error(traceback.format_exc())
    #     else:
    #         pass
    #
    # open_file()
    th = pa + "Log/my_debug.log"
    print(os.path.exists(th))

