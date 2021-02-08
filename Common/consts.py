#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：consts.py
"""
import platform
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Common", "") + "Params")  # Common目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Common", "") + "Config")  # Config目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Common", "") + "Test_case")  # Test_case目录

# 对请求进行伪装
json_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36",
               "Content-Type": "application/json"}

from_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36",
               "Content-Type": "application/x-www-form-urlencoded"}

xml_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36",
              "Content-Type": "text/xml"}

file_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                             "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/84.0.4147.105 Safari/537.36",
               "Content-Type": "multipart/form-data"}

Dealer_Host = "http://api.erp.shopmell.com"
Admin_Host = "http://api.admin.shopmell.com"


def admin_link_os():
    """
    :return: 根据当前操作系统返回相应的地址
    """
    op_sy = platform.platform()
    if "Windows" in op_sy:
        return "http://api.admin.shopmell.com"
    elif "Linux" in op_sy:
        return "http://api.admin.shopmell.com"
    else:
        return op_sy, "未知系统"
