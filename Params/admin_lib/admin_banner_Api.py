#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_banner_Api.py
@Time: 13:59
@Tool: PyCharm
"""
# Banner
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
from Params.admin_lib.file_manage import FileManage


class BannerApi:
    """广告图"""

    def __init__(self):
        self.cookie = Cookie

    def banner_list(self):
        """所有的banner"""
        resp = request(url=f"{Admin_Host}/admin/banner/list", method="POST", headers=json_header, cookies=self.cookie)
        return resp

    def banner_add(self, url, method, in_body):
        """添加广告图"""
        pay = json.loads(in_body)
        pay['uri'] = FileManage("image/image.jpg").get_uri()
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self.cookie)
        return resp

    def banner_enable(self, url, method, banner_id):
        """启用"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[banner_id], headers=json_header, cookies=self.cookie)
        return resp

    def banner_edit(self, url, method, in_body, banner_id):
        """编辑banner"""
        in_body = json.loads(in_body)
        in_body['id'] = banner_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def banner_discontinue(self, url, method, banner_id):
        """停用"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[banner_id], headers=json_header, cookies=self.cookie)
        return resp

    def banner_page(self, url, method, in_body):
        """搜索"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def banner_del(self, url, method, banner_id):
        """删除"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[banner_id], headers=json_header, cookies=self.cookie)
        return resp


if __name__ == '__main__':
    def banner_id():
        exl = ReadExcel(API_admin_path, "banner").auto_dynamic("banner_enable")
        query = BannerApi().banner_page(
            url="/admin/banner/page", method="POST",
            in_body='''{"isEnable": -1,"pageNo": 1,"pageSize": 100,"title": ""}''').json()['data']['data']
        for j in query:
            print(j)
        for i in query:
            print(i)
            if i['title'] in exl:
                return i['id']

    print(banner_id())

    data = 1




