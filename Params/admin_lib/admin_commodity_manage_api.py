#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_commodity_manage_api.py
@Time: 18:00
@Tool: PyCharm
"""
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_cookies import Cookie


class GoodsCategory:
    """商品分类"""

    def __init__(self):
        self._cookie = Cookie

    def list_classify(self, url, method):
        """列出所有分类"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def add_classify(self, url, method, in_body):
        """添加分类"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def add_classify2(self, url, method, in_body, parent_id):
        """添加分类2"""
        pay = json.loads(in_body)
        pay['parentId'] = parent_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def add_classify3(self, url, method, in_body, parent1_id, parent2_id):
        """添加分类3"""
        pay = json.loads(in_body)
        pay['parent'] = parent1_id
        pay['parentId'] = parent2_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def list_display(self, url, method):
        """列出当前的热门显示"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def add_display(self, url, method, parent_id):
        """添加热门显示，保留原有的"""
        now_list = []
        now = self.list_display(url="/admin/product/category/template/list/display", method="POST")
        if now.json()['data']:
            for i in now.json()['data']:
                now_list.append(i["id"])
        now_list.append(parent_id)
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=now_list, headers=json_header, cookies=self._cookie)
        return resp

    def cancel_display(self, url, method, parent_id):
        """取消热门显示"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[parent_id], headers=json_header, cookies=self._cookie)
        return resp

    def edit_classify(self, url, method, in_body, first_id, second_id, third_id):
        """编辑分类"""
        pay = json.loads(in_body)
        pay['firstId'] = first_id
        pay["secondId"] = second_id
        pay["thirdId"] = third_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def page_classify(self, url, method, in_body):
        """分页"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def del_classify(self, url, method, classify_id):
        """删除分类"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[classify_id], headers=json_header, cookies=self._cookie)
        return resp


class CommodityAudit(GoodsCategory):
    """商品审核"""
    ...


class BrandLabel(GoodsCategory):
    """商品标签"""
    def add_tag(self, url, method, in_body):
        """添加标签"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def list_tag(self, url, method):
        """列出所有标签"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def page_tag(self, url, method, in_body):
        """分页显示"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def edit_tag(self, url, method, in_body, tag_id):
        """编辑标签"""
        pay = json.loads(in_body)
        pay['id'] = tag_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def del_tag(self, url, method, tag_id):
        """删除标签"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[tag_id], headers=json_header, cookies=self._cookie)
        return resp


class Model3D(GoodsCategory):
    """3D模型"""

    def add_model(self, url, method, in_body, display_id):
        """添加模型"""
        pay = json.loads(in_body)
        pay['productCategoryId'] = display_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def list_model(self, url, method):
        """列出所有模型"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def page_model(self, url, method, in_body):
        """分页查询"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def rad_model(self, url, method, model_id):
        """读取单个模型"""
        resp = request(url=f"{Admin_Host}{url}{model_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def edit_model(self, url, method, in_body, model_id):
        """编辑模型"""
        pass

    def del_model(self, url, method, model_id):
        """删除模型"""
        resp = request(url=f"{Admin_Host}{url}{model_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp


class TheModelMaterial(GoodsCategory):
    """模型素材"""

    def add_material(self, url, method, in_body):
        """添加素材"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def read_material(self, url, method, material_id):
        """读取单个素材"""
        resp = request(url=f"{Admin_Host}{url}{material_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def page_material(self, url, method, in_body):
        """分页查询"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def edit_material(self, url, method, in_body, material_id):
        """编辑素材"""
        body = json.loads(in_body)
        body['id'] = material_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=body, headers=json_header, cookies=self._cookie)
        return resp

    def list_material(self, url, method):
        """列出所有素材"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def del_material(self, url, method, material_id):
        """删除模型"""
        resp = request(url=f"{Admin_Host}{url}", data=[material_id], method=method, headers=json_header, cookies=self._cookie)
        return resp


if __name__ == '__main__':
    from Params.tools.read_tools import ReadExcel, API_admin_path
    from Params.tools.read_tools import switch_data
    print(TheModelMaterial().edit_material(
        url="/admin/material/library/template/edit", method="POST",
        in_body="""{"id": 0,"name": ""test material","uri": "0948efd4c2691db458a8420416646870.png"}""",
        material_id=58
    ))


