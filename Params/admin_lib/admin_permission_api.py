#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/25
@IDEName： PyCharm
@FileName：admin_permission_api.py
"""
# 权限管理模块
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.return_cookies import Cookie


class PermissionListApi:
    """权限列表"""
    def __init__(self):
        self._cookie = Cookie

    def permission_list(self, url, method):
        """列出所有权限"""
        res = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return res

    def permission_add(self, url, method, in_body):
        """添加权限"""
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self._cookie
        )
        return res

    def permission_page(self, url, method, in_body):
        """分页查询"""
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self._cookie
        )
        return res

    def permission_edit(self, url, method, in_body, pe_id):
        """编辑权限"""
        in_body = json.loads(in_body)
        in_body['id'] = pe_id
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie
        )
        return res

    def permission_del(self, url, method, pe_id):
        """删除权限"""
        res = request(
            url=f"{Admin_Host}{url}{pe_id}", method=method, headers=json_header, cookies=self._cookie
        )
        return res


class RoleListApi(PermissionListApi):
    """角色列表"""
    def role_list(self, url, method):
        """列出所有角色"""
        res = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return res

    def role_add(self, url, method, in_body):
        """添加角色"""
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self._cookie
        )
        return res

    def role_page(self, url, method, in_body):
        """分页查询"""
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self._cookie
        )
        return res

    def role_bind(self, url, method, in_body, uid):
        """角色绑定/取消权限"""
        in_body = json.loads(in_body)
        in_body['roleId'] = uid
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie
        )
        return res

    def role_edit(self, url, method, in_body, uid):
        """编辑/冻结角色"""
        in_body = json.loads(in_body)
        in_body['id'] = uid
        res = request(
            url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie
        )
        return res

    def role_read(self, url, method, uid):
        """查看角色"""
        res = request(
            url=f"{Admin_Host}{url}{uid}", method=method, headers=json_header, cookies=self._cookie
        )
        return res

    def role_del(self, url, method, uid):
        """删除角色"""
        res = request(url=f"{Admin_Host}{url}{uid}", method=method, headers=json_header, cookies=self._cookie)
        return res


if __name__ == '__main__':
    def role_id():
        """查询出用户的ID"""
        dc = {}
        query = RoleListApi().role_page(url="/admin/role/page", method="POST",
                                        in_body='''{"name": "", "pageNo": 1, "pageSize": 10}''').json()['data']['data']
        exl = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("role_edit")
        exl2 = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("role_bind")
        exl3 = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("role_off_bind")
        exl4 = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("role_freeze")
        for i in exl:
            for j in query:
                if j['name'] == i:
                    dc[j['name']] = j['id']
        for i in exl2:
            for j in query:
                if j['name'] == i:
                    dc[j['name']] = j['id']
        for i in exl3:
            for j in query:
                if j['name'] == i:
                    dc[j['name']] = j['id']
        for i in exl4:
            for j in query:
                if j['name'] == i:
                    dc[j['name']] = j['id']
        return dc

    print(role_id())





