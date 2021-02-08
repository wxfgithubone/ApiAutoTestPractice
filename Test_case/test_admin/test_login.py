#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：     2020/10/8 9:33
@Author:    wangxf
@Email:     1845719332@qq.com
@Software： PyCharm
@FileName： test_login.py
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_login_api import LoginApi


@allure.epic("admin接口自动化项目")
@allure.feature("A - 登录")
@allure.suite("登录接口套件")
class TestLogin:

    @allure.story("登录测试")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             ReadExcel(API_admin_path, "login").auto_excel_read("login", body_col=9))
    def test_login(self, title, priority, url, describe, method, payload, test_step, expected):
        res = LoginApi().login(method=method, url=url, in_body=payload)
        assert res['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', '-v', "test_login.py"])



