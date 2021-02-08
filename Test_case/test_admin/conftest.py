#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：     2020/10/8 9:32
@Author:    wangxf
@Email:     1845719332@qq.com
@Software： PyCharm
@FileName： conftest.py
环境的初始化与清除
"""
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path, switch_data
from Params.admin_lib.file_manage import FileManage
from Params.admin_lib.admin_banner_Api import BannerApi
from Params.admin_lib.admin_order_manage import OrderManageApi
from Params.admin_lib.admin_permission_api import PermissionListApi, RoleListApi
from Params.admin_lib.admin_design_manage_Api import DesignGroupApi, DesignListApi
from Params.admin_lib.admin_enterprise_admin_api import DepartmentAdminApi, StaffAdminApi
from Params.admin_lib.admin_member_center_api import MemberListApi, MemberAttributeApi, LevelAdminApi
from Params.admin_lib.admin_article_manage_Api import ArticleClassApi, ArticleTagManageApi, ArticleListApi
from Params.admin_lib.admin_pod_price_api import PriceSetting, MailedPackagePrice
from Params.admin_lib.admin_commodity_manage_api import GoodsCategory, BrandLabel, CommodityAudit, Model3D,\
    TheModelMaterial
from Params.admin_lib.admin_logistics_manage_Api import LogisticsMessageApi, CommercePlatformApi, CommonCarrierApi,\
    PriceSheetApi, ShipperApi


# --------------------企业管理--------------------------
@pytest.fixture(scope="function")
def department_id():
    """编辑企业部门，企业员工编辑绑定部门初始化操作"""
    query = DepartmentAdminApi().department_list(
        method="POST", url="/admin/department/list"
    )
    data_li = query.json()['data']
    dc = {}
    exl = ReadExcel(API_admin_path, "enterprise_admin").auto_dynamic("department_edit")
    exl2 = ReadExcel(API_admin_path, "enterprise_admin").auto_dynamic("staff_add")
    exl3 = ReadExcel(API_admin_path, "enterprise_admin").auto_dynamic("department_del")
    for i in data_li:
        for j in exl:
            if i['name'] == j:
                dc[i['name']] = i['id']
        for k in exl2:
            if i['name'] == k:
                dc[i['name']] = i['id']
        for v in exl3:
            if i['name'] == v:
                dc[i['name']] = i['id']
    return dc


@pytest.fixture(scope="function")
def staff_id():
    """获取员工ID"""
    query = StaffAdminApi().staff_list(url="/admin/staff/list", method="POST").json()['data']
    exl = ReadExcel(API_admin_path, "enterprise_admin").auto_dynamic("staff_edit")
    exl2 = ReadExcel(API_admin_path, "enterprise_admin").auto_dynamic("staff_del")
    dc = dict()
    for i in exl:
        sp = i.split(",")
        for j in query:
            if j['name'] == sp[1]:
                dc[j['name']] = j['id']
    for i in exl2:
        for j in query:
            if j['name'] == i:
                dc[j['name']] = j['id']
    return dc


# ---------------会员中心-----------------
@pytest.fixture(scope="function")
def get_class_id():
    """获取等级ID"""
    dc = dict()
    query = LevelAdminApi().member_list(url="/admin/level/list", method="POST").json()['data']
    exl = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_level_edit")
    exl2 = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_level_del")
    for i in exl:
        for j in query:
            if j['name'] == i:
                dc[j['name']] = j['id']
    for i in exl2:
        for j in query:
            if j['name'] == i:
                dc[j['name']] = j['id']
    return dc


@pytest.fixture(scope="function")
def get_user_id():
    """获取用户ID，字典储存"""
    dc = {}
    query = MemberListApi().member_list(url="/admin/user/list", method="POST").json()['data']
    exl = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_list_edit")
    exl2 = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_list_modify_price")
    exl3 = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_list_edit")
    exl4 = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_list_freeze")
    for i in exl:
        for j in query:
            if j['account'] == i:
                dc[j['account']] = j['id']
    for i in exl2:
        for j in query:
            if j['account'] == i:
                dc[j['account']] = j['id']
    for i in exl3:
        for j in query:
            if j['account'] == i:
                dc[j['account']] = j['id']
    for i in exl4:
        for j in query:
            if j['account'] == i:
                dc[j['account']] = j['id']
    return dc


@pytest.fixture(scope="function")
def role_bind_level_id():
    """用户绑定等级初始化操作 获取用户ID和等ID"""
    dc = dict()
    query = MemberListApi().member_list(
        url="/admin/user/list", method="POST").json()['data']
    query2 = LevelAdminApi().member_list(url="/admin/level/list", method="POST").json()['data']
    print(query)
    exl = ReadExcel(API_admin_path, "member_center").auto_dynamic("member_list_bind_level")
    for i in exl:
        sp = i.split(",")
        for j in query:
            if j['account'] == sp[1]:
                dc[j['account']] = j['id']  # 用户ID
        for k in query2:
            if k['name'] == sp[0]:
                dc[k['name']] = k['id']  # 等级ID
    return dc


@pytest.fixture(scope='function')
def attribute_id():
    """会员属性"""
    query = MemberAttributeApi().member_attribute_page(
        url="/admin/user/attribute/page", method="POST",
        in_body='''{"beginCreateTime":"","endCreateTime":"","userId":0,"pageNo":1,"pageSize":1000}'''
    ).json()['data']['data'][0]['id']
    return query


@pytest.fixture(scope="function")
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


# ----------------------权限管理----------------------
@pytest.fixture(scope="function")
def edit_permission_id():
    """编辑权限 - 对比excel返回对应ID"""
    query = PermissionListApi().permission_list(
        url="/admin/permission/list", method="POST"
    ).json()['data']
    dc = dict()
    exl = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("permission_edit")
    exl2 = ReadExcel(API_admin_path, "permission_admin").auto_dynamic("permission_del")
    for i in exl:
        for j in query:
            if j['name'] == i:
                dc[j['name']] = j['id']
    for i in exl2:
        for j in query:
            if j['name'] == i:
                dc[j['name']] = j['id']
    return dc


@pytest.fixture(scope="function")
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


# -----------------设计管理------------------
@pytest.fixture(scope="function")
def design_group_id():
    """获取设计分组的ID"""
    query = DesignGroupApi().group_list().json()['data']
    exl = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_group_edit")
    exl2 = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_list_add")
    for j in query:
        if j['name'] in exl or j['name'] in exl2:
            return j['id']


@pytest.fixture(scope="function")
def design_message_id():
    """获取设计信息的ID"""
    query = DesignListApi().design_list().json()['data']
    exl = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_list_edit")
    exl2 = ReadExcel(API_admin_path, "design_manage").auto_dynamic("design_list_del")
    for i in query:
        if i['name'] in exl or i['name'] in exl2:
            return i['id']


# ---------------文章管理------------
@pytest.fixture(scope="function")
def article_class_id():
    """获取文章分类的ID"""
    query = ArticleClassApi().article_class_page(
        url="/admin/article/category/page", method="POST",
        in_body='''{"beginCreateTime":"","endCreateTime":"","pageNo":1,"pageSize":100}'''
    ).json()['data']['data']
    exl = ReadExcel(API_admin_path, "article_manage").auto_dynamic("article_class_edit")
    for i in exl:
        for j in query:
            if j['name'] == i:
                return j['id']


@pytest.fixture(scope="function")
def article_tag_id():
    """获取标签ID"""
    query = ArticleTagManageApi().tag_manage_page(
        url="/admin/article/tag/page", method="POST",
        in_body='''{"beginCreateTime":"","endCreateTime":"","pageNo":1,"pageSize":100}'''
    ).json()['data']['data']
    exl = ReadExcel(API_admin_path, "article_manage").auto_dynamic("tag_manage_edit")
    for i in exl:
        for j in query:
            if j['name'] == i:
                return j['id']


@pytest.fixture(scope="function")
def article_class_id2():
    """获取文章分类的ID  字典取值"""
    dc = {}
    query = ArticleClassApi().article_class_page(
        url="/admin/article/category/page", method="POST",
        in_body='''{"beginCreateTime":"","endCreateTime":"","pageNo":1,"pageSize":100}'''
    ).json()['data']['data']
    exl = ReadExcel(API_admin_path, "article_manage").auto_dynamic("article_list_add")
    exl2 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("video_list_add")
    exl3 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("text_list_ad")
    for j in query:
        if j['name'] in exl or j['name'] in exl2 or j['name'] in exl3:
            dc[j['name']] = j['id']
    return dc


@pytest.fixture(scope="function")
def article_id():
    """获取教程的ID"""
    dc = {}
    query = ArticleListApi().article_list().json()['data']
    exl = ReadExcel(API_admin_path, "article_manage").auto_dynamic("article_list_published")
    exl2 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("video_list_published")
    exl3 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("text_list_published")
    for i in query:
        if i['title'] in exl or i['title'] in exl2 or i['title'] in exl3:
            dc[i['title']] = i['id']
    return dc


@pytest.fixture(scope="function")
def article_edit():
    """获取分类ID 和 教程ID"""
    dc = {}
    class_page = ArticleClassApi().article_class_page(
        url="/admin/article/category/page", method="POST",
        in_body='''{"beginCreateTime":"","endCreateTime":"","pageNo":1,"pageSize":100}'''
    ).json()['data']['data']
    list_query = ArticleListApi().article_list().json()['data']
    exl = ReadExcel(API_admin_path, "article_manage").auto_dynamic("article_list_edit")
    exl2 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("video_list_edit")
    exl3 = ReadExcel(API_admin_path, "article_manage").auto_dynamic("text_list_edit")
    for e1 in exl:
        sp = e1.split(",")
        for cl1 in class_page:
            if sp[0] == cl1['name']:
                dc[cl1['name']] = cl1['id']
        for qu1 in list_query:
            if sp[1] == qu1['title']:
                dc[qu1['title']] = qu1['id']
    for e2 in exl2:
        sp = e2.split(",")
        for cl1 in class_page:
            if sp[0] == cl1['name']:
                dc[cl1['name']] = cl1['id']
        for qu1 in list_query:
            if sp[1] == qu1['title']:
                dc[qu1['title']] = qu1['id']
    for e3 in exl3:
        sp = e3.split(",")
        for cl1 in class_page:
            if sp[0] == cl1['name']:
                dc[cl1['name']] = cl1['id']
        for qu1 in list_query:
            if sp[1] == qu1['title']:
                dc[qu1['title']] = qu1['id']
    return dc


# ---------Banner------------
@pytest.fixture(scope="function")
def banner_id():
    exl = ReadExcel(API_admin_path, "banner").auto_dynamic("banner_enable")
    query = BannerApi().banner_page(
        url="/admin/banner/page", method="POST",
        in_body='''{"isEnable": -1,"pageNo": 1,"pageSize": 100,"title": ""}''').json()['data']['data']
    for i in query:
        if i['title'] in exl:
            return i['id']


# -----------物流管理----------
@pytest.fixture(scope="function")
def get_platform_id():
    """获取电商平台ID"""
    dc = {}
    query = CommercePlatformApi().platform_page(url="/admin/platform/template/page", method="POST",
                                                in_body='''{"pageSize":1000,"pageNo":1}''').json()['data']['data']
    exc = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("ec_platform_edit")
    exc2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("ec_platform_del")
    for i in exc:
        for j in query:
            if j['chineseName'] == i:
                dc[j['chineseName']] = j['id']
    for i in exc2:
        for j in query:
            if j['chineseName'] == i:
                dc[j['chineseName']] = j['id']
    return dc


@pytest.fixture(scope="function")
def get_carrier_id():
    """获取承运商ID"""
    dc = {}
    query = CommonCarrierApi().carrier_page(
        url="/admin/platform/carrier/template/page",
        method="POST", in_body='''{"platformId":"","pageSize":1000,"pageNo":1}''').json()['data']['data']
    exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("carrier_platform_edit")
    exl2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("carrier_platform_read")
    for i in exl:
        sp = i.split(",")
        for j in query:
            if j['chineseName'] == sp[0]:
                dc[j['chineseName']] = j['id']
    for i in exl2:
        for j in query:
            if j['chineseName'] == i:
                dc[j['chineseName']] = j['id']
    return dc


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function")
def get_channel_id(get_logistics_id):
    """获取物流公司下的物流渠道ID"""
    dc = {}
    log_exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("logistics_channel_list")
    exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_read")
    exl2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_stop")
    exl3 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("channel_start")
    for i in log_exl:
        query = LogisticsMessageApi().logistics_channel_list(
            url="/admin/logistics/channel/template/list/", method="POST",
            logistics_id=get_logistics_id[i]).json()['data']
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


@pytest.fixture(scope="function")
def get_freight_id():
    """获取报价单ID"""
    dc = {}
    query = PriceSheetApi().freight_list(url="/admin/freight/list", method="POST").json()['data']
    exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("freight_read")
    exl2 = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("freight_edit")
    for j in query:
        for i in exl:
            if j['name'] == i:
                dc[j['name']] = j['id']
        for i in exl2:
            if j['name'] == i:
                dc[j['name']] = j['id']
    return dc


@pytest.fixture(scope="function")
def get_shipper_id(get_channel_id):
    """获取发货人ID"""
    dc = {}
    shipper_exl = ReadExcel(API_admin_path, "logistics_manage").auto_dynamic("shipper_read")
    query = ShipperApi().shipper_list(url="/admin/consigner/list", method="POST").json()['data']
    for i in shipper_exl:
        qu_dao_id = get_channel_id[i]
        for j in query:
            if j['logisticsChannelId'] == qu_dao_id:
                dc[i] = j['id']
    return dc


# -----------------文件管理-----------------
@pytest.fixture(scope="function")
def get_file_id():
    """获取文件id"""
    ...


# ---------商品管理-----------
commodity_manage_excel = ReadExcel(API_admin_path, "commodity_manage").lead_params()


@pytest.fixture(scope="function")
def get_goods_classify_id():
    """获取商品分类的ID"""
    dc_ru = {}
    classify_list = GoodsCategory().list_classify(url="/admin/product/category/template/list", method="POST").json()['data']
    for data in commodity_manage_excel:
        dct = switch_data(data)
        for key, value in dct.items():
            for classify in classify_list:
                classify_name = classify['name']
                if classify_name == value:
                    dc_ru[classify_name] = classify['id']
    return dc_ru


@pytest.fixture(scope="function")
def get_tag_id():
    """获取标签id"""
    dc_ru = {}
    tag_list = BrandLabel().list_tag(url="/admin/tag/list/product", method="POST").json()['data']
    for data in commodity_manage_excel:
        dct = switch_data(data)
        for key, value in dct.items():
            for tag in tag_list:
                tag_name = tag['name']
                if tag_name == value:
                    dc_ru[tag_name] = tag['id']
    return dc_ru


@pytest.fixture(scope="function")
def get_model_id():
    """获取模型id"""
    dc_ru = {}
    model_list = Model3D().list_model(url="/admin/product/customization/template/list", method="POST").json()['data']
    for data in commodity_manage_excel:
        dct = switch_data(data)
        for key, value in dct.items():
            for model in model_list:
                product_name = model['productName']
                if product_name == value:
                    dc_ru[product_name] = model['id']
    return dc_ru


@pytest.fixture(scope="function")
def get_material_id():
    """获取模型素材id"""
    dc_ru = {}
    material_list = TheModelMaterial().list_material(url="/admin/material/library/template/list", method="POST").json()['data']
    excel = ReadExcel(API_admin_path, "commodity_manage").lead_params()
    for data in excel:
        dct = switch_data(data)
        for key, value in dct.items():
            for material in material_list:
                product_name = material['name']
                if product_name == value:
                    dc_ru[product_name] = material['id']
    return dc_ru


# -------------POD价格--------------
pod_price_excel = ReadExcel(API_admin_path, "POD_price").lead_params()


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function")
def get_wu_liu_id(get_price_id):
    """获取当前产品里的物流渠道id"""
    dc_ru, dc_ru2 = {}, {}
    exc = ReadExcel(API_admin_path, "POD_price").auto_dynamic("list_item_price")
    for i in exc:
        dc = switch_data(i)
        for key, value in dc.items():
            item_id = get_price_id[value]
            item_list = MailedPackagePrice().list_item_price(
                url="/admin/cost/price/item/list", method="POST",
                in_body='''{"costPriceId": 0,"dealerId": 0}''', price_id=item_id).json()['data']
            for li in item_list:
                dc_ru[li['freightName']] = li['freightId']
                dc_ru2[li['freightName']] = li['id']
    return dc_ru2, dc_ru

