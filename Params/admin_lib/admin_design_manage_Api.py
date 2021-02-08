#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_design_manage_Api.py
@Time: 17:30
@Tool: PyCharm
"""
# 设计管理
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


class DesignGroupApi:
    """设计分组"""
    def __init__(self):
        self.cookie = Cookie

    def group_list(self):
        """查询所有的分组"""
        resp = request(
            method="POST", url=f"{Admin_Host}/admin/material/group/template/list",
            headers=json_header, cookies=self.cookie)
        return resp

    def group_add(self, url, method, in_body):
        """添加设计分组"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}", data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def group_page(self, url, method, in_body):
        """搜索设计分组"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}", data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def group_edit(self, url, method, in_body, group_id):
        """编辑设计分组"""
        in_body = json.loads(in_body)
        in_body["id"] = group_id
        resp = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def group_del(self, url, method, group_id):
        """删除分组"""
        resp = request(method=method, url=f"{Admin_Host}{url}", data=[group_id], headers=json_header, cookies=self.cookie)
        return resp


class DesignListApi(DesignGroupApi):
    """设计列表"""

    def design_list(self):
        """查询所有设计"""
        resp = request(
            method="POST", url=f"{Admin_Host}/admin/material/template/list", headers=json_header, cookies=self.cookie)
        return resp

    def design_add(self, url, method, in_body, group_id):
        """添加设计"""
        in_body = json.loads(in_body)
        in_body['material']['materialGroupTemplateId'] = group_id
        resp = request(method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def design_edit(self, url, method, in_body, group_id, design_id):
        """编辑设计"""
        in_body = json.loads(in_body)
        in_body['material']['id'] = design_id
        in_body['material']['materialGroupTemplateId'] = group_id
        if in_body['materialVariants']:
            in_body['materialVariants'][0]['id'] = design_id
            resp = request(
                method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)
        else:
            resp = request(
                method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def design_page(self, url, method, in_body, group_id=None):
        """搜索"""
        in_body = json.loads(in_body)
        if "materialGroupTemplateId" in in_body.keys():
            in_body['materialGroupTemplateId'] = group_id
            resp = request(
                method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)
        else:
            resp = request(
                method=method, url=f"{Admin_Host}{url}", data=in_body, headers=json_header, cookies=self.cookie)

        return resp

    def design_del(self, url, method, design_id):
        """删除"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}", data=[design_id], headers=json_header, cookies=self.cookie)
        return resp


if __name__ == '__main__':
    def design_group_id():
        """获取设计分组的ID"""
        query = DesignGroupApi().group_list().json()['data']
        exl = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_group_edit")
        exl2 = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_list_add")
        for j in query:
            if j['name'] in exl or j['name'] in exl2:
                return j['id']

    print(design_group_id())
