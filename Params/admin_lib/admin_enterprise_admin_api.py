#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/23
@IDEName： PyCharm
@FileName：admin_enterprise_admin_api.py
"""
# 企业管理模块
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_cookies import Cookie


class DepartmentAdminApi:
    """企业部门管理"""
    def __init__(self):
        self._cookie = Cookie

    def department_list(self, method, url):
        """企业部门 - 查询所有部门"""
        resp = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return resp

    def department_add(self, method, url, in_body):
        """企业部门 - 增加"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def department_edit(self, method, url, in_body, dep_id):
        """企业部门 - 编辑"""
        in_body = json.loads(in_body)
        in_body['id'] = dep_id
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def department_delete(self, method, url, dep_id):
        """企业部门 - 删除部门"""
        rep = request(method=method, url=f"{Admin_Host}{url}", data=[dep_id], headers=json_header, cookies=self._cookie)
        return rep

    def department_page(self, method, url, in_body):
        """企业部门 - 分页"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep


class StaffAdminApi(DepartmentAdminApi):
    """企业员工管理"""

    def staff_list(self, method, url):
        """企业员工 - 查询所有员工"""
        rep = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return rep

    def staff_add(self, method, url, in_body, dep_id):
        """企业员工 - 增加"""
        in_body = json.loads(in_body)
        in_body['departmentId'] = dep_id
        rep = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def staff_edit(self, method, url, in_body, dep_id, sta_id):
        """企业员工 - 编辑"""
        in_body = json.loads(in_body)
        in_body['departmentId'] = dep_id
        in_body['id'] = sta_id
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep

    def staff_delete(self, method, url, sta_id):
        """企业员工 - 删除员工"""
        rep = request(method=method, url=f"{Admin_Host}{url}", data=[sta_id], headers=json_header, cookies=self._cookie)
        return rep

    def staff_page(self, method, url, in_body):
        """企业员工 - 分页查询员工"""
        rep = request(
            method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self._cookie)
        return rep


if __name__ == '__main__':
    ...
