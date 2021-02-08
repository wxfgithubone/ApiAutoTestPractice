#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/23
@IDEName： PyCharm
@FileName：admin_home_page_api.py
"""
# 首页模块
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_cookies import Cookie
from Params.admin_lib.return_time import GetTimeYMD
from Common.log import logger


class HomePageApi:

    def __init__(self):
        self._cookie = Cookie
        self.time = GetTimeYMD()

    def financial_overview(self, method, url, in_body, data_time):
        """财务总览"""
        try:
            if in_body == '':
                rep = request(
                    method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
            else:
                pay = json.loads(in_body)
                if data_time == '七':
                    pay['beginCreateTime'] = self.time.seven_day()
                    pay['endCreateTime'] = self.time.yesterday()
                elif data_time == '三十':
                    pay['beginCreateTime'] = self.time.thirty_day()
                    pay['endCreateTime'] = self.time.yesterday()
                elif data_time == '一':
                    pay['beginCreateTime'] = self.time.today()
                    pay['endCreateTime'] = self.time.today()
                elif data_time == 'week':
                    pay['beginCreateTime'] = self.time.this_week_start()
                    pay['endCreateTime'] = self.time.this_week_end()
                elif data_time == 'month':
                    pay['beginCreateTime'] = self.time.this_month_start()
                    pay['endCreateTime'] = self.time.this_month_end()
                rep = request(
                    method=method, url=f"{Admin_Host}{url}", data=pay, headers=json_header, cookies=self._cookie)
            return rep
        except BaseException as err:
            logger.error(err)


if __name__ == '__main__':
    ...
