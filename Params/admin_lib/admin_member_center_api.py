#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/26
@IDEName： PyCharm
@FileName：admin_member_center_api.py
"""
# 会员中心模块
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_cookies import Cookie
from Params.tools.read_tools import ReadExcel, API_admin_path


class MemberListApi:
    """会员列表"""
    def __init__(self):
        self._cookie = Cookie

    def member_list(self, url, method):
        """查询所有用户"""
        rep = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return rep

    def member_add(self, url, method, in_body):
        """添加用户"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=json.loads(in_body), headers=json_header, cookies=self._cookie)
        return rep

    def member_page(self, url, method, in_body):
        """分页查询"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=json.loads(in_body), headers=json_header, cookies=self._cookie)
        return rep

    def member_role_bind(self, url, method, in_body, uid):
        """用户绑定角色"""
        in_body = json.loads(in_body)
        in_body['userId'] = uid
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def member_bind_level(self, url, method, in_body, le_id, uid):
        """用户绑定等级"""
        in_body = json.loads(in_body)
        in_body['levelId'] = le_id
        in_body['userId'] = uid
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def member_modify_price(self, url, method, in_body, uid):
        """设置大客户"""
        in_body = json.loads(in_body)
        in_body['id'] = uid
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def member_edit(self, url, method, in_body, uid):
        """编辑用户"""
        in_body = json.loads(in_body)
        in_body['id'] = uid
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def member_freeze(self, method, url, user_id):
        """冻结用户"""
        resp = request(url=f"{Admin_Host}{url}{user_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def member_del(self, method, url, user_id):
        """删除用户"""
        resp = request(url=f"{Admin_Host}{url}{user_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp


class MemberAttributeApi(MemberListApi):

    def member_attribute_all(self, url, method):
        """查询所有权益"""
        rep = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return rep

    def member_attribute_page(self, method, url, in_body):
        """会员权益 - 分页"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=json.loads(in_body), headers=json_header, cookies=self._cookie)
        return rep

    def member_attribute_read(self, method, url, uid):
        """查看单个会员权益"""
        rep = request(method=method, url=f"{Admin_Host}{url}{uid}", headers=json_header, cookies=self._cookie)
        return rep

    def member_attribute_edit(self, method, url, in_body, uid):
        """编辑会员权益"""
        in_body = json.loads(in_body)
        in_body['id'] = uid
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep


class LevelAdminApi(MemberListApi):
    """等级管理"""
    def member_level_all(self, url, method):
        """查询所有等级"""
        rep = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return rep

    def member_level_add(self, url, method, in_body):
        """添加"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", headers=json_header, data=json.loads(in_body), cookies=self._cookie)
        return rep

    def member_level_edit(self, url, method, in_body, level_id):
        """编辑"""
        in_body = json.loads(in_body)
        in_body['id'] = level_id
        rep = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, data=in_body, cookies=self._cookie)
        return rep

    def member_level_page(self, url, method, in_body):
        """分页"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", headers=json_header, data=json.loads(in_body), cookies=self._cookie)
        return rep

    def member_level_del(self, url, method, le_id):
        """删除等级"""
        resp = request(url=f"{Admin_Host}{url}{le_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp


if __name__ == '__main__':
    def quan_yi_id():
        """权益列表的用户ID"""
        query = MemberAttributeApi().member_attribute_page(
            url="/admin/user/attribute/page", method="POST",
            in_body='''{"beginCreateTime":"","endCreateTime":"","userId":0,"pageNo":1,"pageSize":1000}'''
        ).json()['data']['data']
        dc = dict()
        exl = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_attribute_edit")
        for i in exl:
            for j in query:
                if j['userName'] == i:
                    dc[j['userName']] = j['id']
        return dc

    print(quan_yi_id())



