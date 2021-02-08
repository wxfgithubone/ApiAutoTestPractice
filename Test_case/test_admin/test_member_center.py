#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/24
@IDEName： PyCharm
@FileName：test_member_center.py
"""
import os, sys, allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
import pytest
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_member_center_api import MemberListApi, MemberAttributeApi, LevelAdminApi

excel_data = ReadExcel(API_admin_path, "member_center")


@allure.epic("admin接口自动化项目")
@allure.feature("会员中心 - 等级管理")
@allure.suite("会员中心 - 等级管理接口套件")
class TestLevelAdmin:

    @allure.story("列出所有等级（经销商/供应商）")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected", 
                             excel_data.auto_excel_read("member_level_all"))
    def test_level_all(self, title, priority, describe, url, method, test_step, expected):
        resp = LevelAdminApi().member_level_all(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加等级")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("member_level_add", body_col=9))
    def test_level_add(self, title, priority,  describe, url, method, payload, test_step, expected):
        resp = LevelAdminApi().member_level_add(url=url, in_body=payload, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑等级")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_level_edit", body_col=9, dynamic_col=10))
    def test_level_edit(
            self, title, priority,  describe, url, method, payload, dynamic, test_step, expected, get_class_id):
        resp = LevelAdminApi().member_level_edit(
            url=url, in_body=payload,  method=method, level_id=get_class_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询接口")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected", 
                             excel_data.auto_excel_read("member_level_page", body_col=9))
    def test_level_page(self, title, priority,  describe, url, method, payload, test_step, expected):
        res = LevelAdminApi().member_level_page(url=url, method=method, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("会员中心 - 会员列表")
@allure.suite("会员中心 - 会员列表接口套件")
class TestMemberList:
    """会员列表"""
    @allure.story("访问list接口列出所有人员")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("member_list_all"))
    def test_member_query_all(self, title, priority,  describe, url, method, test_step, expected):
        """会员列表 - 列出所有人员"""
        res = MemberListApi().member_list(url=url, method=method)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("新增会员接口")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("member_list_add", body_col=9))
    def test_member_add(self, title, priority,  describe, url, method, payload, test_step, expected):
        res = MemberListApi().member_add(url=url, method=method, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询接口")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("member_list_page", body_col=9))
    def test_member_page(self, title, priority,  describe, url, method, payload, test_step, expected):
        """根据用例对应参数进行分页查询"""
        res = MemberListApi().member_page(url=url, method=method, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("用户绑定角色接口")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_list_role_bind", body_col=9, dynamic_col=10))
    def test_member_role_bind(
            self, title, priority,  describe, url, method, payload, dynamic, test_step, expected, get_user_id):
        res = MemberListApi().member_role_bind(url=url, method=method, in_body=payload, uid=get_user_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("用户绑定等级接口")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_list_bind_level", body_col=9, dynamic_col=10))
    def test_member_bind_level(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, role_bind_level_id):
        res = MemberListApi().member_bind_level(
            url=url, method=method, in_body=payload,
            uid=role_bind_level_id[dynamic.split(',')[1]], le_id=role_bind_level_id[dynamic.split(',')[0]])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("设置大客户")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_list_modify_price", body_col=9, dynamic_col=10))
    def test_member_modify_price(
            self, describe, priority, title, url, method, payload, dynamic, test_step, expected, get_user_id):
        res = MemberListApi().member_modify_price(url=url, method=method, in_body=payload, uid=get_user_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑会员")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_list_edit", body_col=9, dynamic_col=10))
    def test_member_edit(
            self, title, priority,  describe, url, method, payload, dynamic, test_step, expected, get_user_id):
        res = MemberListApi().member_edit(url=url, method=method, in_body=payload, uid=get_user_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("会员中心 - 会员权益")
@allure.suite("会员中心 - 会员权益接口套件")
class TestMemberAttribute:

    @allure.story("分页查询")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, test_step, expected",
        excel_data.auto_excel_read("member_attribute_page", body_col=9))
    def test_member_attribute_page(self, title, priority,  describe, url, method, payload, test_step, expected):
        res = MemberAttributeApi().member_attribute_page(url=url, method=method, in_body=payload)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查看单个会员权益")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, test_step, expected",
        excel_data.auto_excel_read("member_attribute_read"))
    def test_member_attribute_read(self, title, priority,  describe, url, method, test_step, expected, attribute_id):
        res = MemberAttributeApi().member_attribute_read(url=url, method=method, uid=attribute_id)
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("修改会员权益")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, payload, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_attribute_edit", body_col=9, dynamic_col=10))
    def test_member_attribute_edit(
            self, title, priority,  describe, url, method, payload, test_step, dynamic, expected, quan_yi_id):
        res = MemberAttributeApi().member_attribute_edit(
            url=url, method=method, in_body=payload, uid=quan_yi_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("会员中心 - 删除操作")
@allure.suite("会员中心 - 删除操作接口套件")
class TestMemberDel:

    @allure.story("冻结用户")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, dynamic, test_step, expected",
        excel_data.auto_excel_read("member_list_freeze", dynamic_col=10))
    def test_member_freeze(self, title, priority,  describe, url, method, dynamic, test_step, expected, get_user_id):
        res = MemberListApi().member_freeze(url=url, method=method, user_id=get_user_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除人员")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "member_center").auto_excel_read("member_list_del", dynamic_col=10))
    def test_member_del(self, title, priority,  describe, url, method, test_step, expected, dynamic, get_user_id):
        res = MemberListApi().member_del(url=url, method=method, user_id=get_user_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除等级")
    @pytest.mark.parametrize(
        "title, priority, describe, url, method, dynamic, test_step, expected",
        ReadExcel(API_admin_path, "member_center").auto_excel_read("member_level_del", dynamic_col=10))
    def test_level_del(self, title, priority,  describe, url, method, dynamic, test_step, expected, get_class_id):
        res = LevelAdminApi().member_level_del(url=url, method=method, le_id=get_class_id[dynamic])
        assert res.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_member_center.py'])


