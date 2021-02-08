#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：admin_login_api.py
"""
# 登录模块
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Test_case")  # Test_case目录
from Common.request import request
from Common.consts import Admin_Host, json_header


class LoginApi:

    def login(self, method, url, in_body):
        """
        登录后将cookie写入yaml文件
        :param method:
        :param url:
        :param in_body:
        :return: 登录响应信息
        """
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header)
        return rep.json()


if __name__ == '__main__':
    print(
        LoginApi().login(method="POST", url="/admin/passport/login",
                         in_body="""{"account":"admin","password":"HUIQMGMM"}""")
    )
