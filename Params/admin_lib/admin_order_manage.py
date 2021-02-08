#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_order_manage.py
@Time: 17:04
@Tool: PyCharm
"""
# 订单管理模块
import os
import sys
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header, Dealer_Host
from Params.admin_lib.return_cookies import Cookie


class OrderManageApi:
    """订单管理"""
    def __init__(self):
        self._cookie = Cookie

    def all_page(self, url, method, in_body):
        """订单管理 -- 全部列表"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self._cookie)
        return resp

    def login_dealer(self):
        """订单管理，添加新数据 -- 登录经销商"""
        url = f"{Dealer_Host}/erp/dealer/passport/login"
        payload = {"account": "lionamz", "password": "ljx@2019"}
        resp = request(url=url, method="POST", data=payload, headers=json_header)
        cookie = {"LJXD_COOKIE_SESSION_NAME": resp.cookies['LJXD_COOKIE_SESSION_NAME']}
        return cookie

    def dealer_upload_order(self, url, method):
        """订单管理，添加新数据 -- 经销商导入订单"""
        # url = f"{Dealer_Host}/erp/dealer/store/product/order/upload/order/73"
        user_file = {"file": ("orderImportTemplate.xls.xlsx",
                              open(r"F:\auto_test\admin_API_Automation\Params\testData\orderImportTemplate.xls.xlsx", "rb"),
                              'application/vnd.ms-excel', {'Expires': '0'})}
        resp = request(url=f"{Admin_Host}{url}", method=method, files=user_file, cookies=self.login_dealer())
        return resp

    def dealer_pending_page(self, url, method, in_body):
        """分页查看订单 - 等待列表"""
        url = f"{Dealer_Host}/erp/dealer/store/product/order/page"
        payload = {
            "storeId": -1, "countryCodes": [], "orderStatus": "PENDING",
            "pageNo": 1, "pageSize": 1000
        }
        resp = request(url=url, method=method, data=in_body, headers=json_header, cookies=self.login_dealer())
        return resp

    def get_order_id(self, fl_path, sh):
        """获取订单等待列表id"""
        order_id = []
        order_number = self.dealer_pending_page().json()['data']['data']
        for i in auto_order_num(file_path=fl_path, sheet_index=sh):
            for j in order_number:
                if j['order']['orderNumber'] == i:
                    order = j['order']['id']
                    order_id.append(order)
        return order_id

    def dealer_bind_design(self, file_path, sheet):
        """匹配设计"""
        res_list = []
        url = f"{Dealer_Host}/erp/dealer/store/product/order/bind/design"
        for i in self.get_order_id(fl_path=file_path, sh=sheet):
            payload = {
                "orderDetailId": 1440, "materialId": 180, "isReplace": 1, "orderId": i, "materialVariantId": 91
            }
            resp = request(url=url, method="POST", data=payload, headers=json_header)
            res_list.append([resp.request.body, resp.json()])
        return res_list

    def dealer_confirm(self, file_path, sheet):
        """确认订单"""
        res_list = []
        url = f"{Dealer_Host}/erp/dealer/store/product/order/confirm"
        for i in self.get_order_id(fl_path=file_path, sh=sheet):
            resp = request(url=url, method="POST", data=[i], headers=json_header)
            res_list.append(resp.json())
        return res_list

    def dealer_confirmed_page(self):
        """分页查看订单 - 确认列表"""
        url = f"{Dealer_Host}/erp/dealer/store/product/order/page"
        payload = {
            "storeId": -1, "countryCodes": [], "orderStatus": "CONFIRM",
            "pageNo": 1, "pageSize": 1000
        }
        resp = request(url=url, method="POST", data=payload, headers=json_header, cookies=self.login_dealer())
        return resp

    def get_order_id2(self, file_path, sh):
        """获取订单确认列表id"""
        order_id = []
        order_number = self.dealer_confirmed_page().json()['data']['data']
        for i in auto_order_num(file_path=file_path, sheet_index=sh):
            for j in order_number:
                if j['order']['orderNumber'] == i:
                    order = j['order']['id']
                    order_id.append(order)
        return order_id

    def dealer_order_submit(self, file_path, freight_id, sheet):
        """提交订单"""
        res_list = []
        url = f"{Dealer_Host}/erp/dealer/store/product/order/submit"
        for i in self.get_order_id2(file_path=file_path, sh=sheet):
            payload = {
                "orderIds": [i], "freightId": freight_id
            }
            resp = request(url=url, json=payload, headers=json_header)
            res_list.append(resp.json())
        return res_list


if __name__ == '__main__':
    api = OrderManageApi()
    print(api.login_dealer())
    print(os.path.exists("../testData/ecxel/orderImportTemplate.xls.xlsx"))
    print(api.dealer_upload_order(url="/erp/dealer/store/product/order/upload/order/73", method="POST").json())


