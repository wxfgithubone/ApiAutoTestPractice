#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_logistics_manage.py
@Time: 2020/10/25
@Tool: PyCharm
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path
from Params.admin_lib.admin_logistics_manage_Api import LogisticsMessageApi, CommercePlatformApi,\
    CommonCarrierApi, PriceSheetApi, ShipperApi

excel_data = ReadExcel(API_admin_path, "logistics_manage")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 电商平台")
@allure.suite("物流管理 - 电商平台接口套件")
class TestCommercePlatform:

    @allure.story("电商平台 - 添加")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_add", body_col=9))
    def test_platform_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = CommercePlatformApi().platform_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("电商平台 - 搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_page", body_col=9))
    def test_platform_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = CommercePlatformApi().platform_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("电商平台 - 编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_edit", body_col=9, dynamic_col=10))
    def test_platform_edit(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_platform_id):
        resp = CommercePlatformApi().platform_edit(
            url=url, method=method, in_body=payload, plat_id=get_platform_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("电商平台 - 查看单个平台")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_read", dynamic_col=10))
    def test_platform_read(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_platform_id):
        resp = CommercePlatformApi().platform_read(url=url, method=method, plat_id=get_platform_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 承运商")
@allure.suite("物流管理 - 承运商接口套件")
class TestCommonCarrier:

    @allure.story("承运商 - 添加")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_add", body_col=9, dynamic_col=10))
    def test_carrier_add(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_platform_id):
        resp = CommonCarrierApi().carrier_add(url=url, method=method, in_body=payload, plat_id=get_platform_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("承运商 - 搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_page", body_col=9))
    def test_carrier_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = CommonCarrierApi().carrier_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("承运商 - 编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_edit", body_col=9, dynamic_col=10))
    def test_carrier_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_carrier_id, get_platform_id):
        resp = CommonCarrierApi().carrier_edit(
            url=url, method=method, in_body=payload, carr_id=get_carrier_id[dynamic.split(",")[0]],
            plat_id=get_platform_id[dynamic.split(",")[1]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("承运商 - 查看单个承运商")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_read", dynamic_col=10))
    def test_carrier_read(self, title, priority, describe, url, method, dynamic, test_step, expected, get_carrier_id):
        resp = CommercePlatformApi().platform_read(url=url, method=method, plat_id=get_carrier_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 物流信息")
@allure.suite("物流管理 - 物流信息接口套件")
class TestLogisticsMessage:

    @allure.story("物流公司 - 添加")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("logistics_add", body_col=9))
    def test_logistics_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = LogisticsMessageApi().logistics_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流公司 - 分页搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("logistics_page", body_col=9))
    def test_logistics_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = LogisticsMessageApi().logistics_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流公司 - 编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("logistics_edit", body_col=9, dynamic_col=10))
    def test_logistics_edit(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_logistics_id):
        resp = LogisticsMessageApi().logistics_edit(
            url=url, method=method, in_body=payload, logistics_id=get_logistics_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流公司 - read")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("logistics_read", dynamic_col=10))
    def test_logistics_read(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_logistics_id):
        resp = LogisticsMessageApi().logistics_read(url=url, method=method, logistics_id=get_logistics_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 添加")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_add", body_col=9, dynamic_col=10))
    def test_channel_add(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                         get_platform_id, get_carrier_id, get_logistics_id):
        spl = dynamic.split(',')
        resp = LogisticsMessageApi().channel_add(
            url=url, method=method, in_body=payload, plat_id=get_platform_id[spl[0]],
            carr_id=get_carrier_id[spl[1]], logistics_id=get_logistics_id[spl[2]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 查看物流公司里的所有渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("logistics_channel_list", dynamic_col=10))
    def test_logistics_channel_list(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_logistics_id):
        resp = LogisticsMessageApi().logistics_channel_list(
            url=url, method=method, logistics_id=get_logistics_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 列出所有渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel_data.auto_excel_read("channel_list_all"))
    def test_channel_list(self, title, priority, describe, url, method, test_step, expected):
        resp = LogisticsMessageApi().channel_list_all(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 查看单个物流渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_read", dynamic_col=10))
    def test_channel_read(self, title, priority, describe, url, method, dynamic, test_step, expected, get_channel_id):
        resp = LogisticsMessageApi().channel_read(url=url, method=method, channel_id=get_channel_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_edit", body_col=9, dynamic_col=10))
    def test_channel_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_channel_id, get_platform_id, get_carrier_id, get_logistics_id):
        spl = dynamic.split(',')
        resp = LogisticsMessageApi().channel_edit(
            url=url, method=method, in_body=payload,
            channel_id=get_channel_id[spl[0]], plat_id=get_platform_id[spl[1]],
            carr_id=get_carrier_id[spl[2]],  logistics_id=get_logistics_id[spl[3]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 启用物流渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_start", dynamic_col=10))
    def test_channel_start(self, title, priority, describe, url, method, dynamic, test_step, expected, get_channel_id):
        resp = LogisticsMessageApi().channel_start(url=url, method=method, channel_id=get_channel_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 报价单")
@allure.suite("物流管理 - 报价单接口套件")
class TestPriceSheet:

    @pytest.mark.skip(reason="报价单无法删除")
    @allure.story("添加报价单")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("freight_add", body_col=9, dynamic_col=10))
    def test_freight_add(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_channel_id):
        resp = PriceSheetApi().freight_add(url=url, method=method, in_body=payload, channel_id=get_channel_id[dynamic])
        assert resp.json()['message'] == expected
        if "," in dynamic:  # 判断是否写入了多个渠道
            spl = dynamic.split(',')
            ls = [get_channel_id[i] for i in spl]
            print(ls)
            resp = PriceSheetApi().freight_add(url=url, method=method, in_body=payload, channel_id=ls)
            assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查看单个报价单")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("freight_read", dynamic_col=10))
    def test_freight_read(self, title, priority, describe, url, method, dynamic, test_step, expected, get_freight_id):
        resp = PriceSheetApi().freight_read(url=url, method=method, freight_id=get_freight_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑报价单")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("freight_edit", body_col=9, dynamic_col=10))
    def test_freight_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_freight_id, get_channel_id):
        spl_all = dynamic.split(',')
        freight_id = spl_all.pop(0)  # 抛出第一个报价单名称
        ls = [get_channel_id[i] for i in spl_all]     # 储存多个渠道ID
        print(ls)
        resp = PriceSheetApi().freight_edit(
            url=url, method=method, in_body=payload, freight_id=get_freight_id[freight_id], channel_id=ls)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("freight_page", body_col=9))
    def test_freight_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = PriceSheetApi().freight_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 发货人")
@allure.suite("物流管理 - 发货人接口套件")
class TestShipper:

    @allure.story("添加发货人")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("shipper_add", body_col=9, dynamic_col=10))
    def test_shipper_add(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                         get_freight_id, get_channel_id, get_logistics_id):
        spl = dynamic.split(',')
        resp = ShipperApi().shipper_add(url=url, method=method, in_body=payload, freight_id=get_freight_id[spl[1]],
                                        channel_id=get_channel_id[spl[0]], logistics_id=get_logistics_id[spl[2]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("查看单个发货人")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("shipper_read", dynamic_col=10))
    def test_shipper_read(self, title, priority, describe, url, method, dynamic, test_step, expected, get_shipper_id):
        resp = ShipperApi().shipper_read(url=url, method=method, shipper_id=get_shipper_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑发货人")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("shipper_edit", body_col=9, dynamic_col=10))
    def test_shipper_read(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_shipper_id, get_freight_id, get_channel_id, get_logistics_id):
        spl = dynamic.split(',')
        print(spl)
        resp = ShipperApi().shipper_edit(url=url, method=method, in_body=payload,
                                         shipper_id=get_shipper_id[spl[0]], channel_id=get_channel_id[spl[0]],
                                         freight_id=get_freight_id[spl[1]], logistics_id=get_logistics_id[spl[2]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("shipper_page", body_col=9))
    def test_shipper_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = ShipperApi().shipper_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("复制发货人")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("shipper_copy", body_col=9, dynamic_col=10))
    def test_shipper_copy(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_shipper_id, get_freight_id, get_channel_id, get_logistics_id):
        spl = dynamic.split(',')
        resp = ShipperApi().shipper_copy(url=url, method=method, in_body=payload,
                                         shipper_id=get_shipper_id[spl[0]], channel_id=get_channel_id[spl[1]],
                                         freight_id=get_freight_id[spl[2]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("物流管理 - 停用、删除")
@allure.suite("物流管理 - 停用、删除接口套件")
class TestLogisticsManageDel:

    @allure.story("删除发货人")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("shipper_del", dynamic_col=10))
    def test_shipper_del(self, title, priority, describe, url, method, dynamic, test_step, expected, get_shipper_id):
        resp = ShipperApi().shipper_del(url=url, method=method, shipper_id=get_shipper_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("停用报价单")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("freight_stop", body_col=9, dynamic_col=10))
    def test_freight_stop(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_freight_id, get_channel_id):
        spl_all = dynamic.split(',')
        freight_id = spl_all.pop(0)  # 抛出第一个报价单名称
        ls = [get_channel_id[i] for i in spl_all]     # 储存多个渠道ID
        print(ls)
        resp = PriceSheetApi().freight_edit(
            url=url, method=method, in_body=payload, freight_id=get_freight_id[freight_id], channel_id=ls)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @pytest.mark.skip(reason="报价单删除无效")
    @allure.story("删除报价单")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("freight_del", dynamic_col=10))
    def test_freight_del(self, title, priority, describe, url, method, dynamic, test_step, expected, get_freight_id):
        resp = PriceSheetApi().freight_del(url=url, method=method, freight_id=get_freight_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 停用物流渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_stop", dynamic_col=10))
    def test_channel_stop(self, title, priority, describe, url, method, dynamic, test_step, expected, get_channel_id):
        resp = LogisticsMessageApi().channel_stop(url=url, method=method, channel_id=get_channel_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流渠道 - 删除物流渠道")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("channel_del", dynamic_col=10))
    def test_channel_del(self, title, priority, describe, url, method, dynamic, test_step, expected, get_channel_id):
        resp = LogisticsMessageApi().channel_del(url=url, method=method, channel_id=get_channel_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流公司 - 停用")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("logistics_stop", body_col=9, dynamic_col=10))
    def test_logistics_stop(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_logistics_id):
        resp = LogisticsMessageApi().logistics_edit(
            url=url, method=method, in_body=payload, logistics_id=get_logistics_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("物流公司 - 删除")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("logistics_del", dynamic_col=10))
    def test_logistics_del(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_logistics_id):
        resp = LogisticsMessageApi().logistics_del(url=url, method=method, logistics_id=get_logistics_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("承运商 - 停用")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_stop", body_col=9, dynamic_col=10))
    def test_carrier_stop(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_carrier_id, get_platform_id):
        resp = CommonCarrierApi().carrier_edit(
            url=url, method=method, in_body=payload, carr_id=get_carrier_id[dynamic.split(",")[0]],
            plat_id=get_platform_id[dynamic.split(",")[1]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("承运商 - 删除")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("carrier_platform_del", dynamic_col=10))
    def test_carrier_del(self, title, priority, describe, url, method, dynamic, test_step, expected, get_carrier_id):
        resp = CommercePlatformApi().platform_del(url=url, method=method, plat_id=get_carrier_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("电商平台 - 停用")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_stop", body_col=9, dynamic_col=10))
    def test_platform_stop(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_platform_id):
        resp = CommercePlatformApi().platform_edit(
            url=url, method=method, in_body=payload, plat_id=get_platform_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("电商平台 - 删除")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("ec_platform_del", dynamic_col=10))
    def test_platform_del(self, title, priority, describe, url, method, dynamic, test_step, expected, get_platform_id):
        resp = CommercePlatformApi().platform_del(url=url, method=method, plat_id=get_platform_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', 'test_logistics_manage.py'])



