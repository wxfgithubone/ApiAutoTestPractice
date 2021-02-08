#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: test_article_manage.py
@Time: 2020/9/24 11:59
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
from Params.admin_lib.admin_article_manage_Api import ArticleClassApi, ArticleTagManageApi, \
    ArticleListApi, VideoListApi, TextListApi

excel_data = ReadExcel(API_admin_path, "article_manage")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 文章分类")
@allure.suite("文章管理 - 文章分类接口套件")
class TestArticleClass:

    @allure.story("添加分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("article_class_add", body_col=9))
    def test_class_add(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = ArticleClassApi().article_class_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("article_class_page", body_col=9))
    def test_class_page(self, title, priority, describe, url, method, payload, test_step, expected):
        resp = ArticleClassApi().article_class_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("article_class_edit", body_col=9))
    def test_class_edit(self, title, priority, describe, url, method, payload, test_step, expected, article_class_id):
        resp = ArticleClassApi().article_class_edit(url=url, method=method, in_body=payload, class_id=article_class_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 标签管理")
@allure.suite("文章管理 - 标签管理接口套件")
class TestArticleManage:

    @allure.story("添加标签")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("tag_manage_add", body_col=9))
    def test_tag_manage_add(self, priority, title, describe, url, method, payload, test_step, expected):
        resp = ArticleTagManageApi().tag_manage_add(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("搜索")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("tag_manage_page", body_col=9))
    def test_tag_manage_page(self, priority, title, describe, url, method, payload, test_step, expected):
        resp = ArticleTagManageApi().tag_manage_page(url=url, method=method, in_body=payload)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, test_step, expected",
                             excel_data.auto_excel_read("tag_manage_edit", body_col=9))
    def test_tag_manage_edit(
            self, title, priority, describe, url, method, payload, test_step, expected, article_tag_id):
        resp = ArticleTagManageApi().tag_manage_edit(url=url, method=method, in_body=payload, tag_id=article_tag_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 文章列表")
@allure.suite("文章管理 - 文章列表接口套件")
class TestArticleList:

    @allure.story("添加文章")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_list_add", body_col=9, dynamic_col=10))
    def test_article_list_add(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                              article_class_id2, article_tag_id):
        resp = ArticleListApi().article_list_add(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic], tag_id=article_tag_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("发布文章")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_list_published", dynamic_col=10))
    def test_article_list_published(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = ArticleListApi().article_list_published(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_list_edit", body_col=9, dynamic_col=10))
    def test_article_list_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                               article_class_id2, article_tag_id, article_id):
        resp = ArticleListApi().article_list_edit(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic.split(",")[0]],
            tag_id=article_tag_id, article_id=article_id[dynamic.split(",")[1]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 视频教程")
@allure.suite("文章管理 - 视频教程接口套件")
class TestVideoList:

    @allure.story("添加视频教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("video_list_add", body_col=9, dynamic_col=10))
    def test_video_list_add(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                            article_class_id2, article_tag_id):
        resp = VideoListApi().video_list_add(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic], tag_id=article_tag_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("发布视频教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("video_list_published", dynamic_col=10))
    def test_video_list_published(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = VideoListApi().video_list_published(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("video_list_edit", body_col=9, dynamic_col=10))
    def test_video_list_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                             article_class_id2, article_tag_id, article_id):
        resp = VideoListApi().video_list_edit(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic.split(",")[0]],
            tag_id=article_tag_id, article_id=article_id[dynamic.split(",")[1]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 文本教程")
@allure.suite("文章管理 - 文本教程接口套件")
class TestTextList:

    @allure.story("取消发布文章")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_list_unpublish", dynamic_col=10))
    def test_article_list_unpublish(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = ArticleListApi().article_list_unpublish(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("添加文本教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("text_list_add", body_col=9, dynamic_col=10))
    def test_text_list_add(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                           article_class_id2, article_tag_id):
        resp = TextListApi().text_list_add(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic], tag_id=article_tag_id)
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("发布文本教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("text_list_published", dynamic_col=10))
    def test_text_list_published(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = TextListApi().text_list_published(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("编辑")
    @pytest.mark.parametrize("title, priority, describe, url, method, payload, dynamic, test_step, expected",
                             excel_data.auto_excel_read("text_list_edit", body_col=9, dynamic_col=10))
    def test_text_list_edit(self, title, priority, describe, url, method, payload, dynamic, test_step, expected,
                            article_class_id2, article_tag_id, article_id):
        resp = TextListApi().text_list_edit(
            url=url, method=method, in_body=payload, class_id=article_class_id2[dynamic.split(",")[0]],
            tag_id=article_tag_id, article_id=article_id[dynamic.split(",")[1]])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 删除")
@allure.suite("文章管理 - 删除接口套件")
class TestCategoryDel:

    @allure.story("删除文章")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_list_del", dynamic_col=10))
    def test_article_list_del(self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = ArticleListApi().article_list_del(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("取消发布视频教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("video_list_unpublish", dynamic_col=10))
    def test_video_list_unpublish(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = VideoListApi().video_list_unpublish(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除视频教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("video_list_del", dynamic_col=10))
    def test_video_list_del(self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = VideoListApi().video_list_del(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("取消发布文本教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("text_list_unpublish", dynamic_col=10))
    def test_text_list_unpublish(
            self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = TextListApi().text_list_unpublish(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除文本教程")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("text_list_del", dynamic_col=10))
    def test_text_list_del(self, title, priority, describe, url, method, dynamic, test_step, expected, article_id):
        resp = VideoListApi().video_list_del(url=url, method=method, article_id=article_id[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")

    @allure.story("删除文章分类")
    @pytest.mark.parametrize("title, priority, describe, url, method, dynamic, test_step, expected",
                             excel_data.auto_excel_read("article_class_del", dynamic_col=10))
    def test_article_class_del(self, title, priority, describe, url, method, dynamic, test_step, expected, article_edit):
        resp = ArticleClassApi().article_class_del(url=url, method=method, class_id=article_edit[dynamic])
        assert resp.json()['message'] == expected
        allure.dynamic.title(title), allure.description(describe)
        allure.dynamic.severity(priority), allure.attach(test_step, "用例步骤")


@pytest.mark.skip(reason="该功能暂未实现")
@allure.epic("admin接口自动化项目")
@allure.feature("文章管理 - 评论")
@allure.suite("文章管理 - 评论接口套件")
class TestCommentList:

    @allure.story("评论")
    @allure.title("查看评论")
    def test_comment_page(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_article_manage.py'])


