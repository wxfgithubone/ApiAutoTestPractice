#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：run.py
"""
import pytest
import os
import shutil

json_path = "./Report/tmp"  # allure报告
for json_file in os.listdir(json_path):
    os.remove(f"{json_path}/{json_file}")

shutil.copy("./Config/environment.xml", "./Report/tmp")
shutil.copy("./Config/categories.json", "./Report/tmp")

pytest.main(['-v', '-s', './Test_case/test_admin/', '--alluredir', './Report/tmp'])
os.system('allure generate ./Report/tmp -o ./Report/report')
os.system('allure serve ./Report/tmp')

# pytest.main(['-v', '-s', './Test_case/test_admin/'])

