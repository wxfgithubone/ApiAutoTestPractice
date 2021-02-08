#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@File: admin_article_manage_Api.py
@Time: 11:59
@Tool: PyCharm
"""
# 文章管理
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


class ArticleClassApi:
    """文章分类"""

    def __init__(self):
        self.cookie = Cookie

    def article_class_add(self, url, method, in_body):
        """添加文章分类"""
        in_body = json.loads(in_body)
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def article_class_page(self, url, method, in_body):
        """文章分类搜索"""
        in_body = json.loads(in_body)
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def article_class_edit(self, url, method, in_body, class_id):
        """编辑文章分类"""
        in_body = json.loads(in_body)
        in_body['id'] = class_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def article_class_del(self, url, method, class_id):
        """删除分类"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[class_id], headers=json_header, cookies=self.cookie)
        return resp


class ArticleTagManageApi(ArticleClassApi):
    """标签管理"""
    def tag_manage_add(self, url, method, in_body):
        """添加标签"""
        in_body = json.loads(in_body)
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def tag_manage_edit(self, url, method, in_body, tag_id):
        """编辑标签"""
        in_body = json.loads(in_body)
        in_body['id'] = tag_id
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def tag_manage_page(self, url, method, in_body):
        """搜索标签"""
        in_body = json.loads(in_body)
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp


class ArticleListApi(ArticleClassApi):
    """文章列表"""
    def article_list(self):
        resp = request(url=f"{Admin_Host}/admin/article/list", method="POST", headers=json_header, cookies=self.cookie)
        return resp

    def article_list_add(self, url, method, in_body, class_id, tag_id):
        """添加文章"""
        in_body = json.loads(in_body)
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def article_list_published(self, url, method, article_id):
        """发布文章"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def article_list_edit(self, url, method, in_body, article_id, class_id, tag_id):
        """编辑文章"""
        in_body = json.loads(in_body)
        in_body['id'] = article_id
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def article_list_unpublish(self, url, method, article_id):
        """取消发布"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def article_list_del(self, url, method, article_id):
        """删除文章"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp


class VideoListApi(ArticleClassApi):
    """视频教程列表"""

    def video_list_add(self, url, method, in_body, class_id, tag_id):
        """添加视频"""
        in_body = json.loads(in_body)
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def video_list_published(self, url, method, article_id):
        """发布视频"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def video_list_edit(self, url, method, in_body, article_id, class_id, tag_id):
        """编辑视频教程"""
        in_body = json.loads(in_body)
        in_body['id'] = article_id
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def video_list_unpublish(self, url, method, article_id):
        """取消发布"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def video_list_del(self, url, method, article_id):
        """删除视频教程"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp


class TextListApi(ArticleClassApi):
    """文本教程列表"""

    def text_list_add(self, url, method, in_body, class_id, tag_id):
        """添加文本教程"""
        in_body = json.loads(in_body)
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def text_list_published(self, url, method, article_id):
        """发布文本教程"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def text_list_edit(self, url, method, in_body, article_id, class_id, tag_id):
        """编辑文本教程"""
        in_body = json.loads(in_body)
        in_body['id'] = article_id
        in_body['articleCategoryId'] = class_id
        in_body['articleTagIds'] = [tag_id]
        resp = request(url=f"{Admin_Host}{url}", method=method, data=in_body, headers=json_header, cookies=self.cookie)
        return resp

    def text_list_unpublish(self, url, method, article_id):
        """取消发布"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp

    def text_list_del(self, url, method, article_id):
        """删除文本教程"""
        resp = request(
            url=f"{Admin_Host}{url}", method=method, data=[article_id], headers=json_header, cookies=self.cookie)
        return resp


class CommentListApi(ArticleClassApi):
    """评论列表"""
    pass


if __name__ == '__main__':
    def article_edit():
        """获取分类ID 和 文章ID"""
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


    print(article_edit())


