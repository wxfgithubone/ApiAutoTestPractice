#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：     2020/10/8 9:51
@Author:    wangxf
@Email:     1845719332@qq.com
@Software： PyCharm
@FileName： test_home_page.py
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_home_page_api import HomePageApi


@allure.epic("admin接口自动化项目")
@allure.feature("首页")
@allure.suite("首页接口套件")
class TestHomePage:

    @allure.story("输入不同的日期进行测试")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "home_page").auto_excel_read("home_financial_summary", body_col=9, dynamic_col=10))
    def test_home_page(self, title, priority, describe, url, method, payload, dynamic, test_step, expected):
        """首页测试"""
        res = HomePageApi().financial_overview(method=method, url=url, in_body=payload, data_time=dynamic)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', '-v', "test_home_page.py"])


