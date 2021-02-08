#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_banner.py
@Time: 2020/10/24 14:00
@Tool: PyCharm
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_banner_Api import BannerApi

excel_data = ReadExcel(API_admin_path, "banner")


@allure.epic("admin接口自动化项目")
@allure.feature("Banner")
@allure.suite("banner接口套件")
class TestBanner:

    @allure.story("添加banner")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("banner_add", body_col=9))
    def test_banner_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = BannerApi().banner_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("启用")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("banner_enable"))
    def test_banner_enable(self, title, priority, describe, url, method, test_step, expected, banner_id):
        resp = BannerApi().banner_enable(url=url, method=method, banner_id=banner_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("banner_edit", body_col=9))
    def test_banner_edit(self, title, priority, describe, url, method, payload, test_step, expected, banner_id):
        resp = BannerApi().banner_edit(url=url, method=method, in_body=payload, banner_id=banner_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("停用")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("banner_discontinue"))
    def test_banner_discontinue(self, title, priority, describe, url, method, test_step, expected, banner_id):
        resp = BannerApi().banner_discontinue(url=url, method=method, banner_id=banner_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("banner_page", body_col=9))
    def test_banner_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = BannerApi().banner_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("banner_del"))
    def test_banner_del(self, title, priority, describe, url, method, test_step, expected, banner_id):
        resp = BannerApi().banner_del(url=url, method=method, banner_id=banner_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_banner.py'])

