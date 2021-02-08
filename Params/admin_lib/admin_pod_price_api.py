#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Author: 王小飞
@File  : admin_pod_price_api.py
@Time  : 2020/12/4 18:25
@Tool  : PyCharm
"""
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_time import GetTimeYMD
from Params.tools.read_tools import ReadExcel, API_admin_path, switch_data
from Params.admin_lib.return_cookies import Cookie


class PriceSetting:
    """价格设定"""
    def __init__(self):
        self._cookie = Cookie

    def add_price(self, url, method, in_body):
        """添加价格设定"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def list_price(self, url, method):
        """列出所有价格产品"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def read_price(self, url, method, price_id):
        """读取单个价格产品"""
        resp = request(url=f"{Admin_Host}{url}{price_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def page_price(self, url, method, in_dody):
        """分页搜索"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_dody, headers=json_header, cookies=self._cookie)
        return resp

    def edit_price(self, url, method, in_body, price_id):
        """编辑价格产品"""
        pay = json.loads(in_body)
        pay['id'] = price_id
        pay['createTime'] = GetTimeYMD().now_time()
        pay['updateTime'] = GetTimeYMD().now_time()
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def del_price(self, url, method, price_id):
        """删除价格产品"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[price_id], headers=json_header, cookies=self._cookie)
        return resp


class MailedPackagePrice:
    """包邮价格设定"""

    def __init__(self):
        self._cookie = Cookie

    def page_mailed_price(self, url, method, in_body):
        """分页查询"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp

    def list_big_customers(self, url, method):
        """查询出当前的大客户"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def list_item_price(self, url, method, in_body, price_id):
        """查询当前产品的物流渠道和报价"""
        pay = json.loads(in_body)
        pay['costPriceId'] = price_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp

    def read_item_price(self, url, method, price_id):
        """读取单个条款"""
        resp = request(url=f"{Admin_Host}{url}{price_id}", method=method, headers=json_header, cookies=self._cookie)
        return resp

    def edit_mailed_price(self, url, method, in_body, freight_id, da_id, price_id):
        """修改单个渠道价格"""
        pay = json.loads(in_body)
        pay['id'] = da_id
        pay['freightId'] = freight_id
        pay['costPriceId'] = price_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=pay, headers=json_header, cookies=self._cookie)
        return resp


class HarmonizedCode:

    def __init__(self):
        self._cookie = Cookie

    def page_harmonized(self, url, method, in_body):
        """分页搜索"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self._cookie)
        return resp


if __name__ == '__main__':
    pod_price_excel = ReadExcel(API_admin_path, "POD_price").lead_params()

    def get_price_id():
        """获取价格设定产品的ID"""
        dc_ru = {}
        price_list = PriceSetting().list_price(url="/admin/cost/price/list", method="POST").json()['data']
        for price_setting in pod_price_excel:
            dc = switch_data(price_setting)
            for key, value in dc.items():
                for price in price_list:
                    price_title = price['title']
                    if price_title == value:
                        dc_ru[price_title] = price['id']
        return dc_ru

    def get_freight_id():
        """获取当前产品里的物流渠道id"""
        dc_ru, dc_ru2 = {}, {}
        exc = ReadExcel(API_admin_path, "POD_price").auto_dynamic("list_item_price")
        for i in exc:
            dc = switch_data(i)
            for key, value in dc.items():
                item_id = get_price_id()[value]
                item_list = MailedPackagePrice().list_item_price(
                    url="/admin/cost/price/item/list", method="POST",
                    in_body='''{"costPriceId": 0,"dealerId": 0}''', price_id=item_id).json()['data']
                for li in item_list:
                    dc_ru[li['freightName']] = li['freightId']
                    dc_ru2[li['freightName']] = li['id']
        return dc_ru2, dc_ru

    print(get_freight_id())

