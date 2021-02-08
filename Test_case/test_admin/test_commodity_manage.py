#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_commodity_manage.py
@Time: 2020/9/24 18:00
@Tool: PyCharm
"""
import sys
import os
import pytest
import allure
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Params")  # Params目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Test_case", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Params.tools.read_tools import ReadExcel, API_admin_path, switch_data
from Params.admin_lib.admin_commodity_manage_api import GoodsCategory, BrandLabel, Model3D, TheModelMaterial

excel = ReadExcel(API_admin_path, "commodity_manage")


@allure.epic("admin接口自动化项目")
@allure.feature("商品管理 - 商品分类")
@allure.suite("商品管理 - 商品分类接口套件")
class TestGoodsCategory:

    @allure.story("列出所有分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel.auto_excel_read("list_classify"))
    def test_list_classify(self, title, priority, describe, url, method, test_step, expected):
        resp = GoodsCategory().list_classify(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加一级分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("add_classify", body_col=9))
    def test_add_classify(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = GoodsCategory().add_classify(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加二级分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("add_2classify", body_col=9, dynamic_col=10))
    def test_add_classify2(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_goods_classify_id):
        one_classify = switch_data(dynamic)['一级分类']
        resp = GoodsCategory().add_classify2(
            url=url, method=method, in_body=payload, parent_id=get_goods_classify_id[one_classify])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加三级分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("add_3classify", body_col=9, dynamic_col=10))
    def test_add_classify3(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_goods_classify_id):
        one_classify, two_classify = switch_data(dynamic)['一级分类'], switch_data(dynamic)['二级分类']
        resp = GoodsCategory().add_classify3(
            url=url, method=method, in_body=payload,
            parent1_id=get_goods_classify_id[one_classify],
            parent2_id=get_goods_classify_id[two_classify])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("列出当前的热门显示")
    @pytest.mark.parametrize("title, priority, describe, url, method, test_step, expected",
                             excel.auto_excel_read("list_display"))
    def test_list_display(self, title, priority, describe, url, method, test_step, expected):
        resp = GoodsCategory().list_classify(url=url, method=method)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加热门显示")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("add_display", dynamic_col=10))
    def test_add_display(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_goods_classify_id):
        classify_name = switch_data(dynamic)['一级分类']
        resp = GoodsCategory().add_display(
            url=url, method=method, parent_id=get_goods_classify_id[classify_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("取消热门显示")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("cancel_display", dynamic_col=10))
    def test_cancel_display(
            self, title, priority, describe, url, method, dynamic, test_step, expected, get_goods_classify_id):
        classify_name = switch_data(dynamic)['一级分类']
        resp = GoodsCategory().cancel_display(
            url=url, method=method, parent_id=get_goods_classify_id[classify_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_classify", body_col=9, dynamic_col=10))
    def test_edit_classify(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_goods_classify_id):
        one_classify, two_classify, three_classify = \
            switch_data(dynamic)['一级分类'], switch_data(dynamic)['二级分类'], switch_data(dynamic)['三级分类']
        resp = GoodsCategory().edit_classify(
            url=url, method=method, in_body=payload, first_id=get_goods_classify_id[one_classify],
            second_id=get_goods_classify_id[two_classify], third_id=get_goods_classify_id[two_classify])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页显示")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_classify", body_col=9))
    def test_page_classify(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = GoodsCategory().page_classify(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("商品管理 - 商品标签")
@allure.suite("商品管理 - 商品标签接口套件")
class TestBrandLabel:

    @allure.story("添加标签")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("add_tag", body_col=9))
    def test_add_tag(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = BrandLabel().add_tag(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_tag", body_col=9))
    def test_page_tag(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = BrandLabel().page_tag(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑标签")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_tag", body_col=9, dynamic_col=10))
    def test_edit_tag(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_tag_id):
        tag_name = switch_data(dynamic)['标签名称']
        resp = BrandLabel().edit_tag(url=url, method=method, in_body=payload, tag_id=get_tag_id[tag_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@pytest.mark.skip(reason="该功能处于调试阶段")
@allure.epic("admin接口自动化项目")
@allure.feature("商品管理 - 3D模型")
@allure.suite("商品管理 - 3D模型接口套件")
class TestModel3D:

    @allure.story("添加3D模型")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("add_3D_model", body_col=9, dynamic_col=10))
    def test_add_3d_model(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_goods_classify_id):
        classify_name = switch_data(dynamic)['商品分类名称']
        resp = Model3D().add_model(
            url=url, method=method, in_body=payload, display_id=get_goods_classify_id[classify_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("读取单个3D模型")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("read_3D_model", dynamic_col=10))
    def test_read_3d_model(self, title, priority, describe, url, method, dynamic, test_step, expected, get_model_id):
        model_name = switch_data(dynamic)['3D模型名称']
        resp = Model3D().rad_model(url=url, method=method, model_id=get_model_id[model_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("add_3D_model", body_col=9))
    def test_page_3d_model(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = Model3D().page_model(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑3D模型")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_3D_model", body_col=9, dynamic_col=10))
    def test_add_3d_model(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                          get_goods_classify_id, get_model_id):
        classify_name = switch_data(dynamic)['商品分类名称']
        model_name = switch_data(dynamic)['3D模型名称']
        resp = Model3D().add_model(
            url=url, method=method, in_body=payload, display_id=get_goods_classify_id[classify_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("商品管理 - 模型素材")
@allure.suite("商品管理 - 模型素材接口套件")
class TestTheModelMaterial:

    @allure.story("添加模型素材")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("add_material", body_col=9))
    def test_add_material(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = TheModelMaterial().add_material(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("读取单个模型素材")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("read_material", dynamic_col=10))
    def test_read_material(self, title, priority, describe, url, method, dynamic, test_step, expected, get_material_id):
        material_name = switch_data(dynamic)['素材名称']
        resp = TheModelMaterial().read_material(url=url, method=method, material_id=get_material_id[material_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("分页查询")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel.auto_excel_read("page_material", body_col=9))
    def test_page_material(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = TheModelMaterial().page_material(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @pytest.mark.skip(reason="该功能暂未实现")
    @allure.story("编辑模型素材")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel.auto_excel_read("edit_material", body_col=9, dynamic_col=10))
    def test_edit_material(
            self, title, priority, describe, url, method, payload, dynamic, test_step, expected, get_material_id):
        material_name = switch_data(dynamic)['素材名称']
        print(material_name)
        resp = TheModelMaterial().edit_material(
            url=url, method=method, in_body=payload, material_id=get_material_id[material_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("商品管理 - 删除操作")
@allure.suite("商品管理 - 删除操作接口套件")
class TestCommodityManageDel:

    @allure.story("删除模型素材")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("del_material", dynamic_col=10))
    def test_del_material(self, title, priority, describe, url, method, dynamic, test_step, expected, get_material_id):
        material_name = switch_data(dynamic)['素材名称']
        resp = TheModelMaterial().del_material(url=url, method=method, material_id=get_material_id[material_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @pytest.mark.skip(reason="该功能处于调试阶段")
    @allure.story("删除3D模型")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("del_3D_model", dynamic_col=10))
    def test_del_model(self, title, priority, describe, url, method, dynamic, test_step, expected, get_model_id):
        model_name = switch_data(dynamic)['3D模型名称']
        resp = Model3D().del_model(url=url, method=method, model_id=get_model_id[model_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除标签")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("del_tag", dynamic_col=10))
    def test_del_tag(self, title, priority, describe, url, method, dynamic, test_step, expected, get_tag_id):
        tag_name = switch_data(dynamic)['标签名称']
        resp = BrandLabel().del_tag(url=url, method=method, tag_id=get_tag_id[tag_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel.auto_excel_read("del_classify", dynamic_col=10))
    def test_del_classify(self, title, priority, describe, url, method, dynamic, test_step, expected, get_goods_classify_id):
        classify_name = switch_data(dynamic)['分类名称']
        resp = GoodsCategory().del_classify(url=url, method=method, classify_id=get_goods_classify_id[classify_name])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.dynamic.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_commodity_manage.py'])

