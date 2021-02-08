#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_logistics_manage_Api.py
@Time: 
@Tool: PyCharm
"""
# 物流管理
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


class LogisticsMessageApi:
    """物流信息"""
    def __init__(self):
        self.cookie = Cookie

    def logistics_add(self, url, method, in_body):
        """添加物流公司"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def logistics_page(self, url, method, in_body):
        """物流公司分页搜索"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def logistics_edit(self, url, method, in_body, logistics_id):
        """编辑物流公司"""
        in_body = json.loads(in_body)
        in_body['id'] = logistics_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def logistics_read(self, url, method, logistics_id):
        """read物流公司"""
        resp = request(url=f"{Admin_Host}{url}{logistics_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def logistics_del(self, url, method, logistics_id):
        """删除物流公司"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[logistics_id], headers=json_header, cookies=self.cookie)
        return resp

    def channel_add(self, url, method, in_body, plat_id, carr_id, logistics_id):
        """添加物流渠道"""
        in_body = json.loads(in_body)
        in_body['logisticsId'] = logistics_id  # 物流
        in_body['channelPlatforms'][0]['platformCarrierId'] = carr_id  # 承运商
        in_body['channelPlatforms'][0]['platformId'] = plat_id  # 平台
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def logistics_channel_list(self, url, method, logistics_id):
        """查看单个物流公司里的所有渠道"""
        resp = request(url=f"{Admin_Host}{url}{logistics_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def channel_list_all(self, url, method):
        """列出所有渠道"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def channel_read(self, url, method, channel_id):
        """查看单个渠道"""
        resp = request(url=f"{Admin_Host}{url}{channel_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def channel_edit(self, url, method, in_body, channel_id, plat_id, carr_id, logistics_id):
        """编辑物流渠道"""
        in_body = json.loads(in_body)
        in_body['id'] = channel_id  # 渠道ID
        in_body['logisticsId'] = logistics_id  # 物流公司
        in_body['channelPlatforms'][0]['platformCarrierId'] = carr_id  # 承运商
        in_body['channelPlatforms'][0]['platformId'] = plat_id  # 平台
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def channel_start(self, url, method, channel_id):
        """启用渠道"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[channel_id], headers=json_header, cookies=self.cookie)
        return resp

    def channel_stop(self, url, method, channel_id):
        """停用渠道"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[channel_id], headers=json_header, cookies=self.cookie)
        return resp

    def channel_del(self, url, method, channel_id):
        """删除渠道"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[channel_id], headers=json_header, cookies=self.cookie)
        return resp


class CommercePlatformApi(LogisticsMessageApi):
    """电商平台"""
    def platform_add(self, url, method, in_body):
        """添加"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def platform_page(self, url, method, in_body):
        """分页搜索"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def platform_edit(self, url, method, in_body, plat_id):
        """编辑"""
        in_body = json.loads(in_body)
        in_body['id'] = plat_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def platform_read(self, url, method, plat_id):
        """停用"""
        resp = request(url=f"{Admin_Host}{url}{plat_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def platform_del(self, url, method, plat_id):
        """删除"""
        resp = request(url=f"{Admin_Host}{url}{plat_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp


class CommonCarrierApi(LogisticsMessageApi):
    """承运商"""
    def carrier_add(self, url, method, in_body, plat_id):
        """添加承运商"""
        in_body = json.loads(in_body)
        in_body['platformId'] = plat_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def carrier_page(self, url, method, in_body):
        """分页搜索"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def carrier_edit(self, url, method, in_body, carr_id, plat_id):
        """编辑"""
        in_body = json.loads(in_body)
        in_body['id'] = carr_id
        in_body['platformId'] = plat_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def carrier_read(self, url, method, carr_id):
        """read"""
        resp = request(url=f"{Admin_Host}{url}{carr_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def carrier_del(self, url, method, carr_id):
        """删除承运商"""
        resp = request(url=f"{Admin_Host}{url}{carr_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp


class PriceSheetApi(LogisticsMessageApi):
    """报价单"""

    def freight_list(self, url, method):
        """列出所有报价单"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def freight_add(self, url, method, in_body, channel_id):
        """添加报价单"""
        in_body = json.loads(in_body)
        in_body['channelIds'] = [channel_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def freight_read(self, url, method, freight_id):
        """查看单个报价单"""
        resp = request(url=f"{Admin_Host}{url}{freight_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def freight_edit(self, url, method, in_body, freight_id, channel_id):
        """编辑报价单"""
        in_body = json.loads(in_body)
        in_body['id'] = freight_id
        in_body['channelIds'] = channel_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def freight_page(self, url, method, in_body):
        """分页搜索"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=json.loads(in_body), headers=json_header, cookies=self.cookie)
        return resp

    def freight_del(self, url, method, freight_id):
        """删除报价单"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=freight_id, headers=json_header, cookies=self.cookie)
        return resp


class ShipperApi(LogisticsMessageApi):
    """发货人"""

    def shipper_list(self, url, method):
        """列出所有发货人"""
        resp = request(url=f"{Admin_Host}{url}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_add(self, url, method, in_body, freight_id, channel_id, logistics_id):
        """添加发货人"""
        in_body = json.loads(in_body)
        in_body['freightId'] = freight_id
        in_body['logisticsChannelId'] = channel_id
        in_body['logisticsId'] = logistics_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_read(self, url, method, shipper_id):
        """查看单个发货人信息"""
        resp = request(url=f"{Admin_Host}{url}{shipper_id}", method=method, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_edit(self, url, method, in_body, shipper_id, freight_id, channel_id, logistics_id):
        """编辑发货人"""
        in_body = json.loads(in_body)
        in_body['id'] = shipper_id
        in_body['freightId'] = freight_id
        in_body['logisticsChannelId'] = channel_id
        in_body['logisticsId'] = logistics_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_page(self, url, method, in_body):
        """分页搜索"""
        in_body = json.loads(in_body)
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_copy(self, url, method, in_body, shipper_id, freight_id, channel_id):
        """复制发货人"""
        in_body = json.loads(in_body)
        in_body['id'] = shipper_id
        in_body['freightId'] = freight_id
        in_body['logisticsChannelId'] = channel_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def shipper_del(self, url, method, shipper_id):
        """删除发货人"""
        resp = request(url=f"{Admin_Host}{url}", method=method, data=[shipper_id], headers=json_header, cookies=self.cookie)
        return resp


if __name__ == '__main__':

    def get_logistics_id():
        """获取物流公司ID"""
        dc = {}
        query = LogisticsMessageApi().logistics_page(
            url="/admin/logistics/template/page", method="POST",
            in_body='''{"pageNo":1,"pageSize":200}''').json()['data']['data']
        exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("logistics_edit")
        exl2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("logistics_read")
        for i in exl:
            for j in query:
                if j['chineseName'] == i:
                    dc[j['chineseName']] = j['id']
        for i in exl2:
            for j in query:
                if j['chineseName'] == i:
                    dc[j['chineseName']] = j['id']
        return dc


    def get_channel_id():
        """获取物流公司下的物流渠道ID"""
        dc = {}
        log_exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("logistics_channel_list")
        exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_read")
        exl2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_stop")
        exl3 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_start")
        for i in log_exl:
            query = LogisticsMessageApi().logistics_channel_list(
                url="/admin/logistics/channel/template/list/", method="POST",
                logistics_id=get_logistics_id()[i]).json()['data']
            for j in query:
                for k in exl:
                    if j['name'] == k:
                        dc[j['name']] = j['id']
                for k in exl2:
                    if j['name'] == k:
                        dc[j['name']] = j['id']
                for k in exl3:
                    if j['name'] == k:
                        dc[j['name']] = j['id']
        return dc

    def get_shipper_id():
        """获取发货人ID"""
        dc = {}
        shipper_exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("shipper_read")
        query = ShipperApi().shipper_list(url="/admin/consigner/list", method="POST").json()['data']
        for i in shipper_exl:
            qu_dao_id = get_channel_id()[i]
            for j in query:
                if j['logisticsChannelId'] == qu_dao_id:
                    print(j)
                    dc[i] = j['id']
        return dc

    print(get_shipper_id())
    print(get_channel_id())

