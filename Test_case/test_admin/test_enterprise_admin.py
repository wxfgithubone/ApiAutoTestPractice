#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：     2020/10/8 10:08
@Author:    wangxf
@Email:     1845819332@qq.com
@Software： PyCharm
@FileName： test_enterprise_admin.py
"""
import sys, os, pytest, allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_enterprise_admin_api import DepartmentAdminApi, StaffAdminApi


@allure.epic("admin接口自动化项目")
@allure.feature("企业管理 - 企业部门")
@allure.suite("企业管理 - 企业部门接口套件")
class TestDepartmentAdmin:

    @allure.story("访问list接口列出所有部门")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("department_list"))
    def test_department_list(self, title, priority, describe, method, url, test_step, expected):
        res = DepartmentAdminApi().department_list(method=method, url=url)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加部门")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("department_add", body_col=9))
    def test_department_add(self, title, priority, describe, url, method, payload, test_step, expected):
        res = DepartmentAdminApi().department_add(method=method, url=url, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑企业部门")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("department_edit", body_col=9, dynamic_col=10))
    def test_department_edit(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, department_id):
        res = DepartmentAdminApi().department_edit(
            method=method, url=url, in_body=payload, dep_id=department_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("对企业部门进行分页测试")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("department_page", body_col=9))
    def test_department_page(self, title, priority, describe, url, method, payload, test_step, expected):
        res = DepartmentAdminApi().department_add(method=method, url=url, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("企业管理 - 企业员工")
@allure.suite("企业管理 - 企业员工接口套件")
class TestStaffAdmin:

    @allure.story("访问list接口列出所有人员")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("staff_list"))
    def test_staff_list(self, title, priority, describe, url, method, test_step, expected):
        """企业员工 - 列出所有"""
        res = StaffAdminApi().staff_list(method=method, url=url)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加员工接口")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("staff_add", body_col=9, dynamic_col=10))
    def test_staff_add(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, department_id):
        """企业员工 - 添加"""
        res = StaffAdminApi().staff_add(method=method, url=url, in_body=payload, dep_id=department_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑员工接口")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("staff_edit", body_col=9, dynamic_col=10))
    def test_staff_edit(self, title, priority, describe, url, method, payload, dynamic,
                        test_step, expected, department_id, staff_id):
        res = StaffAdminApi().staff_edit(
            method=method, url=url, in_body=payload,
            dep_id=department_id[dynamic.split(',')[0]], sta_id=staff_id[dynamic.split(',')[1]])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询接口")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("staff_page", body_col=9))
    def test_staff_page(self, title, priority, describe, url, method, payload, test_step, expected):
        """企业员工 - 分页"""
        res = StaffAdminApi().staff_page(method=method, url=url, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("企业管理 - 部门、员工删除操作")
@allure.suite("企业管理 - 部门、员工删除操作接口套件")
class TestEnterpriseDel:

    @allure.story("员工删除")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("staff_del", dynamic_col=10))
    def test_staff_del(self, title, priority, describe, url, method, dynamic, test_step, expected, staff_id):
        res = StaffAdminApi().staff_delete(method=method, url=url, sta_id=staff_id[dynamic])
        if res.json()['message']:
            assert res.json()['message'] == expected
        else:
            raise KeyError
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("部门删除")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "enterprise_admin").auto_excel_read("department_del", dynamic_col=10))
    def test_department_del(self, title, priority, describe, url, method, dynamic, test_step, expected, department_id):
        res = DepartmentAdminApi().department_delete(method=method, url=url, dep_id=department_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_enterprise_admin.py'])






