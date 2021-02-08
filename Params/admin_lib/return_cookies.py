#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/28
@IDEName： PyCharm
@FileName：return_cookies.py
"""
# 返回登录后的cookie
import requests
from json import JSONDecodeError
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
from Common.log import logger
from Common.consts import Admin_Host

url = f"{Admin_Host}/admin/passport/login"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                        "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36",
          "Content-Type": "application/json"}
in_body = {"account": "admin", "password": "HUIQMGMM"}
try:
    reps = requests.post(url=url, json=in_body, headers=header)
except JSONDecodeError:
    logger.error(JSONDecodeError)
except BaseException as err:
    logger.error(err)
else:
    Cookie = {"LJXA_COOKIE_SESSION_NAME": reps.cookies['LJXA_COOKIE_SESSION_NAME']}


if __name__ == '__main__':
    print(Cookie)

