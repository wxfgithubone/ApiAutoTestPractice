#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：     2020/10/9 14:40
@Author:    wangxf
@Email:     1845719332@qq.com
@Software： PyCharm
@FileName： cop.py
"""
import os
import shutil

_path = "/var/lib/jenkins/workspace/dir_auto_test/execute-the-test-admin/allure_report"
for _file in os.listdir(_path):
    filePath = os.path.join(_path, _file)  # 映射为文件的绝对路径
    if os.path.isfile(filePath):  # 判断是文件或文件夹
        os.remove(filePath)
    elif os.path.isdir(filePath):
        shutil.rmtree(filePath, True)  # 删除文件夹内所有文件

# 复制配置文件
shutil.copy("/home/auto_test/admin_API/Config/environment.xml", _path)
shutil.copy("/home/auto_test/admin_API/Config/categories.json", _path)
