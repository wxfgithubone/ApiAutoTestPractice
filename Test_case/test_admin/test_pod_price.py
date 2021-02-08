#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Author: 王小飞
@File  : test_pod_price.py
@Time  : 2020/12/4 18:28
@Tool  : PyCharm
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path, switch_data
from Params.admin_lib.admin_pod_price_api import PriceSetting, MailedPackagePrice, HarmonizedCode

excel = ReadExcel(API_admin_path, "POD_price")


@allure.epic("admin接口自动化项目")
@allure.feature("POD价格 - 价格设定")
@allure.suite("POD价格 - 价格设定接口套件")
class TestPriceSetting:

    @allure.story("添加产品")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("add_price", body_col=9))
    def test_add_price(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = PriceSetting().add_price(url=url, method=method, in_body=payload).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("列出所有产品")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel.auto_excel_read("list_price"))
    def test_list_price(self, title, priority, describe, url, method, test_step, expected):
        resp = PriceSetting().list_price(url=url, method=method).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("读取单个产品")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("read_price", dynamic_col=10))
    def test_read_price(self, title, priority, describe, url, method, dynamic, test_step, expected, get_price_id):
        price_name = switch_data(dynamic)['产品名称']
        resp = PriceSetting().read_price(url=url, method=method, price_id=get_price_id[price_name]).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_price", body_col=9))
    def test_page_price(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = PriceSetting().page_price(url=url, method=method, in_dody=payload).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑产品")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_price", body_col=9, dynamic_col=10))
    def test_edit_price(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_price_id):
        price_name = switch_data(dynamic)['产品名称']
        resp = PriceSetting().edit_price(url=url, method=method, in_body=payload, price_id=get_price_id[price_name]).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("POD价格 - 包邮价格")
@allure.suite("POD价格 - 包邮价格接口套件")
class TestMailedPackagePrice:

    @allure.story("分页查询")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_mailed_price", body_col=9))
    def test_page_mailed_price(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = MailedPackagePrice().page_mailed_price(url=url, method=method, in_body=payload).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查询大客户人数")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel.auto_excel_read("list_big_customers"))
    def test_page_mailed_price(self, title, priority, describe, url, method, test_step, expected):
        resp = MailedPackagePrice().list_big_customers(url=url, method=method).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查看价格详细")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("list_item_price", body_col=9, dynamic_col=10))
    def test_list_item_price(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_price_id):
        price_name = switch_data(dynamic)['产品名称']
        resp = MailedPackagePrice().list_item_price(
            url=url, method=method, in_body=payload, price_id=get_price_id[price_name]).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @pytest.mark.skip(reason="不确定！")
    @allure.story("读取单个条款")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("list_big_customers", dynamic_col=10))
    def test_page_mailed_price(self, title, priority, describe, url, method, dynamic, test_step, expected, get_price_id):
        price_name = switch_data(dynamic)['产品名称']
        resp = MailedPackagePrice().read_item_price(url=url, method=method, price_id=get_price_id[price_name]).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑价格")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_mailed_price", body_col=9, dynamic_col=10))
    def test_edit_mailed_price(self, title, priority, describe, url, method, payload, dynamic,
                               test_step, expected, get_wu_liu_id, get_price_id):
        price_name = switch_data(dynamic)['产品名称']
        freight_name = switch_data(dynamic)['渠道名称']
        resp = MailedPackagePrice().edit_mailed_price(
            url=url, method=method, in_body=payload, da_id=get_wu_liu_id[0][freight_name],
            freight_id=get_wu_liu_id[1][freight_name], price_id=get_price_id[price_name]).json()
        assert resp['message'] == expected and resp['code'] == 200
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("POD价格 - 海关编码")
@allure.suite("POD价格 - 海关编码接口套件")
class TestHarmonizedCode:

    @allure.story("分页搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_harmonized", body_col=9))
    def test_page_harmonized(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = HarmonizedCode().page_harmonized(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("POD价格 - 删除操作")
@allure.suite("POD价格 - 删除操作接口套件")
class PodPriceDel:

    @allure.story("删除价格")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("", dynamic_col=10))
    def test_del_price(self, title, priority, describe, url, method, dynamic, test_step, expected):
        pass


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_pod_price.py'])


