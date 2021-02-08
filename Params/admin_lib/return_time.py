#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: return_time.py
@Time: 
@Tool: PyCharm
"""
import datetime
import calendar
from datetime import timedelta


class GetTimeYMD:

    def __init__(self):
        self._now_time = datetime.datetime.now()
        self._today = datetime.date.today()

    def today(self):
        """今天"""
        time = str(self._now_time).split(' ')[0]
        return time

    def yesterday(self):
        """昨天"""
        time = str(self._now_time - timedelta(days=1)).split(' ')[0]
        return time

    def seven_day(self):
        """七天前"""
        time = str(self._today + datetime.timedelta(days=-7))
        return time

    def thirty_day(self):
        """30天前"""
        time = str(self._today + datetime.timedelta(days=-30))
        return time

    def this_week_start(self):
        """本周第一天"""
        time = str(self._now_time - timedelta(days=self._now_time.weekday())).split(' ')[0]
        return time

    def this_week_end(self):
        """本周最后一天"""
        time = str(self._now_time + timedelta(days=6 - self._now_time.weekday())).split(' ')[0]
        return time

    def this_month_start(self):
        """本月第一天"""
        time = str(datetime.datetime(self._now_time.year, self._now_time.month, 1)).split(' ')[0]
        return time

    def this_month_end(self):
        """本月最后一天"""
        time = calendar.monthrange(self._now_time.year, self._now_time.month)[1]
        return "{}-{}-{}".format(self._now_time.year, self._now_time.month, time)

    def now_time(self):
        """当前时间 时分秒"""
        time = str(self._now_time).split(".")[0]
        return time


if __name__ == '__main__':
    da = GetTimeYMD()
    for i in range(10):
        da.today()
    # print(da.now_time())
    # """
    # 2020-12-03 16:17:07
    # 2020-12-03 16:24:36.363918
    # """
    # str1 = "python "
    # str2 = "python"
    # print(str1.rstrip())
    # print(str2.rstrip())
    # print(str1.replace(" ", ""))










