#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_design_manage.py
@Time: 2020/9/25 9:30
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
from Params.admin_lib.admin_design_manage_Api import DesignGroupApi, DesignListApi

excel_data = ReadExcel(API_admin_path, "design_manage")


@allure.epic("admin接口自动化项目")
@allure.feature("设计管理 - 设计分组")
@allure.suite("设计管理 - 设计分组接口套件")
class TestDesignGroup:

    @allure.story("添加分组")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_group_add", body_col=9))
    def test_group_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = DesignGroupApi().group_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("搜索设计分组")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_group_page", body_col=9))
    def test_group_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = DesignGroupApi().group_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑设计分组")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_group_edit", body_col=9))
    def test_group_page(self, title, priority, describe, url, method, payload, expected, test_step, design_group_id):
        resp = DesignGroupApi().group_edit(url=url, method=method, in_body=payload, group_id=design_group_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("设计管理 - 设计列表")
@allure.suite("设计管理 - 设计列表接口套件")
class TestDesignList:

    @allure.story("添加设计")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_list_add", body_col=9))
    def test_design_add(self, title, priority, describe, url, method, payload, test_step, expected, design_group_id):
        resp = DesignListApi().design_add(url=url, method=method, in_body=payload, group_id=design_group_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑设计")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_list_edit", body_col=9))
    def test_design_edit(self, title, priority, describe, url, method, payload, test_step, expected,
                         design_message_id, design_group_id):
        resp = DesignListApi().design_edit(
            url=url, method=method, in_body=payload, group_id=design_group_id, design_id=design_message_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("design_list_page", body_col=9))
    def test_design_page(self, title, priority, describe, url, method, payload, test_step, expected, design_group_id):
        resp = DesignListApi().design_page(url=url, method=method, in_body=payload, group_id=design_group_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("设计管理 - 删除")
@allure.suite("设计管理 - 删除接口套件")
class TestDesignDel:

    @allure.story("删除设计")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("design_list_del"))
    def test_design_del(self, title, priority, describe, url, method, test_step, expected, design_message_id):
        resp = DesignListApi().design_del(url=url, method=method, design_id=design_message_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除分组")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("design_group_del"))
    def test_group_del(self, title, priority, describe, url, method, test_step, expected, design_group_id):
        resp = DesignGroupApi().group_del(url=url, method=method, group_id=design_group_id).json()
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_design_manage.py'])

