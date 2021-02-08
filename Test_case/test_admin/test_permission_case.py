#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/24
@IDEName： PyCharm
@FileName：test_permission_case.py
"""
import os, sys, allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
import pytest
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_permission_api import PermissionListApi, RoleListApi

excel_data = ReadExcel(API_admin_path, "permission_admin")


@allure.epic("admin接口自动化项目")
@allure.feature("权限管理 - 权限列表")
@allure.suite("权限管理 - 权限列表接口套件")
class TestPermissionList:
    """权限列表"""
    @allure.story("列出权限")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("permission_list"))
    def test_permission_list(self, title, priority, describe, url, method, test_step, expected):
        resp = PermissionListApi().permission_list(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加权限")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("permission_add", body_col=9))
    def test_permission_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = PermissionListApi().permission_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("permission_page", body_col=9))
    def test_permission_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = PermissionListApi().permission_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑权限接口")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("permission_edit", body_col=9, dynamic_col=10))
    def test_permission_edit(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, edit_permission_id):
        resp = PermissionListApi().permission_edit(
            url=url, method=method, in_body=payload, pe_id=edit_permission_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("权限管理 - 角色列表")
@allure.suite("权限管理 - 角色列表接口套件")
class TestRoleList:
    """角色列表"""
    @allure.story("列出所有角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("role_list"))
    def test_role_list(self, title, priority, describe, url, method, test_step, expected):
        resp = RoleListApi().role_list(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("role_add", body_col=9))
    def test_role_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = RoleListApi().role_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("role_page", body_col=9))
    def test_role_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = RoleListApi().role_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("角色绑定权限")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_bind", body_col=9, dynamic_col=10))
    def test_role_bind(self, title, priority, describe, url, method, payload, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_bind(
            url=url, method=method, in_body=payload, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("角色取消绑定权限")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_off_bind", body_col=9, dynamic_col=10))
    def test_role_off_bind(self, title, priority, describe, url, method, payload, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_bind(
            url=url, method=method, in_body=payload, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查看角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_read", dynamic_col=10))
    def test_role_read(self, title, priority, describe, url, method, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_read(url=url, method=method, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_edit", body_col=9, dynamic_col=10))
    def test_role_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_edit(url=url, method=method, in_body=payload, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("权限管理 - 删除操作")
@allure.suite("权限管理 - 删除操作接口套件")
class TestPermissionDel:

    @allure.story("冻结角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_freeze", body_col=9, dynamic_col=10))
    def test_role_freeze(self, title, priority, describe, url, method, payload, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_edit(
            url=url, method=method, in_body=payload, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除角色")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("role_del", dynamic_col=10))
    def test_role_del(self, title,priority,  describe, url, method, dynamic, test_step, expected, role_id):
        resp = RoleListApi().role_del(url=url, method=method, uid=role_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除权限接口")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("permission_del", dynamic_col=10))
    def test_permission_del(
            self, title, priority, describe, url, method, dynamic, test_step, expected, edit_permission_id):
        resp = PermissionListApi().permission_del(url=url, method=method, pe_id=edit_permission_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_permission_case.py'])
