#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_order_manage.py
@Time: 2020/9/24 17:32
@Tool: PyCharm
"""
import os, sys, allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
import pytest
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_order_manage import OrderManageApi

excel_data = ReadExcel(API_admin_path, "orders_manage")


@pytest.mark.skip(reason="该功能暂未实现")
@allure.epic("admin接口自动化项目")
@allure.feature("订单管理")
@allure.suite("订单管理接口套件")
class TestOrderManage:

    @allure.story("全部列表")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("all_page", body_col=9))
    def test_all_page(self, title, priority, describe, url, method, payload, test_step, expected):
        """订单管理 - 全部列表"""
        resp = OrderManageApi().all_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("经销商系统导入订单")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, test_step, expected",
        excel_data.auto_excel_read("dealer_upload"))
    def test_dealer_upload_order(self, title, priority, describe, url, method, test_step, expected):
        """经销商导入订单"""
        resp = OrderManageApi().dealer_upload_order(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_order_manage.py'])


