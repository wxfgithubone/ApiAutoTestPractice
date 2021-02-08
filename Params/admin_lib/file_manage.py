#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Author: 王小飞
@File  : file_manage.py
@Time  : 2020/11/28 10:46
@Tool  : PyCharm
"""
#  文件管理的公共方法
import os
import sys
import hashlib
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Common")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Params", "") + "Config")  # Config目录
from Common.request import request
from Common.consts import Admin_Host, json_header
from Params.admin_lib.return_cookies import Cookie
from Config.read_config import yaml_conf_read, YamlHandler

home_path = os.path.dirname(__file__).replace("admin_lib", "testData") + "/"


class FileManage:
    """
    MD5加密文件内容（字节），
    将加密后的MD5值当做资源识别符上传到七牛云，
    将文件后缀名与MD5值拼接
    """
    yaml_data = YamlHandler(yaml_conf_read).read_config()
    QiNiuUrl = yaml_data['URL']['QiNiu']

    def __init__(self, file_name):
        self._cookie = Cookie
        self.fileName = file_name

    def get_file_suffix(self):
        """获取文件的后缀"""
        suffix = self.fileName.split(".")[-1]
        return ".{}".format(suffix)

    def get_file_format(self):
        """获取文件格式"""
        file_format = self.fileName.split("/")[-1]
        file = file_format.split(".")[-1]
        return file

    def get_file_name(self):
        """获取文件名称"""
        file_name = self.fileName.split("/")[-1]
        return file_name

    def get_file_type(self):
        """获取文件类型"""
        file_type = self.fileName.split("/")[0]
        return file_type

    def file_md5(self):
        """文件md5加密"""
        md = hashlib.md5()
        with open(f"{home_path}{self.fileName}", "rb") as f:
            while True:
                data = f.read()
                if len(data) == 0:
                    break
                md.update(data)
        return md.hexdigest()

    def get_token(self, method="POST", url="/admin/file/token"):
        """获取token"""
        resp = request(method=method, url=f"{Admin_Host}{url}", headers=json_header, cookies=self._cookie)
        return resp.json()

    def up_qi_niu(self, method="POST", url=QiNiuUrl):
        """上传到七牛云，根据传入的参数获取文件类型、名称、参数类型"""
        files = {
            'file': (
                self.get_file_name(),
                open(f"{home_path}{self.fileName}", "rb"),
                f"{self.get_file_type()}/{self.get_file_format()}"
            )
        }
        body = {
            "token": self.get_token()['data'],
            "key": "{0}{1}".format(self.file_md5(), self.get_file_suffix())
        }
        resp = request(method=method, url=url, params_type="FROM", data=body, files=files)
        return resp.json()

    def file_type(self):
        """返回文件类型， int"""
        fi_type = self.fileName.split("/")[0]
        if fi_type == "image":
            int_type = 1
            return int_type
        elif fi_type == "video":
            int_type = 2
            return int_type
        elif fi_type == "file":
            int_type = 3
            return int_type

    def add_file(self, method="POST", url=f"/admin/file/add"):
        """添加文件"""
        body = {"fileCategoryId": 0, "md5": self.file_md5(),
                "name": self.get_file_name(), "suffix": self.get_file_suffix(),
                "type": self.file_type(), "uri": f"{self.file_md5()}{self.get_file_suffix()}"}
        resp = request(method=method, url=f"{Admin_Host}{url}", data=body, headers=json_header, cookies=self._cookie)
        return resp.json()

    def find_file(self, method="POST", url="/admin/file/page"):
        """查找上传的文件"""
        body = {"fileCategoryId": 0, "md5": self.file_md5(), "name": "", "pageNo": 1,
                "pageSize": 10, "suffix": "", "type": self.file_type()}
        resp = request(
            method=method, url=f"{Admin_Host}{url}", data=body, headers=json_header, cookies=self._cookie
        )
        return resp.json()['data']['data']

    def edit_file(self, method="POST", url="/admin/file/edit"):
        """编辑文件"""
        body = {"fileCategoryId": 0, "id": self.find_file()[0]['id'], "md5": self.file_md5(),
                "name": self.get_file_name(), "suffix": self.get_file_suffix(), "type": self.file_type(),
                "uri": f"{self.file_md5()}{self.get_file_suffix()}"}
        resp = request(method=method, url=f"{Admin_Host}{url}", data=body, headers=json_header, cookies=self._cookie)
        return resp.json()

    def read_file(self, method="POST", url="/admin/file/read/"):
        """读取文件"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}{self.find_file()[0]['id']}",
            headers=json_header, cookies=self._cookie
        )
        return resp.json()

    def del_file(self, method="POST", url="/admin/file/delete/"):
        """删除文件"""
        resp = request(
            method=method, url=f"{Admin_Host}{url}{self.find_file()[0]['id']}",
            headers=json_header, cookies=self._cookie
        )
        return resp.json()

    def get_uri(self):
        """获取文件的uri"""
        if self.find_file():
            return f"{self.file_md5()}{self.get_file_suffix()}"
        else:
            self.up_qi_niu()
            self.add_file()
            return f"{self.file_md5()}{self.get_file_suffix()}"


if __name__ == '__main__':
    api = FileManage("video/video.3gp")
    print(FileManage("video/video.3gp").up_qi_niu())  # 上传七牛云
    # print(FileManage("video/video.3gp").get_token())  # 获取token
    # print("MD5 " + FileManage("image/test.jpg").file_md5())  # 获得MD5值
    # print(FileManage("video/video.3gp").edit_file())
    # print(FileManage("image/timg.jpg").get_uri())
    print(FileManage("video/video.3gp").add_file())  # 添加文件
    print(api.find_file())
    # print(api.get_uri())
    # print(api.del_file())


