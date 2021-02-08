#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Author: 王小飞
@File  : test_file_manage.py
@Time  : 2020/11/28 17:20
@Tool  : PyCharm
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.admin_lib.file_manage import FileManage, home_path
from Params.tools.read_tools import ReadExcel, API_admin_path

excel = ReadExcel(API_admin_path, "file_manage")
image = os.listdir(f"{home_path}image/")
video = os.listdir(f"{home_path}video/")


@allure.epic("admin接口自动化项目")
@allure.feature("文件管理")
@allure.suite("文件管理接口套件")
class TestFileManage:

    @allure.story("生成token")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("get_token", dynamic_col=10))
    def test_get_token(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).get_token(method=method, url=url)
        print(resp['data'])
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("文件上传七牛云")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("up_qi_niu", dynamic_col=10))
    def test_file_up_qi_niu(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).up_qi_niu(method=method, url=url)
        assert expected in resp['key']
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加文件")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("add_file", dynamic_col=10))
    def test_add_file(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).add_file(method=method, url=url)
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查找文件")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("find_file", dynamic_col=10))
    def test_find_file(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).find_file(method=method, url=url)
        print(resp)
        assert resp[0]['name'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("读取文件")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("read_file", dynamic_col=10))
    def test_read_file(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).read_file(method=method, url=url)
        print(resp)
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑文件")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_file", dynamic_col=10))
    def test_edit_file(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).edit_file(method=method, url=url)
        print(resp)
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除文件")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("del_file", dynamic_col=10))
    def test_del_file(self, title, priority, describe, url, method, dynamic, test_step, expected):
        resp = FileManage(dynamic).del_file(method=method, url=url)
        assert resp['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_file_manage.py'])

