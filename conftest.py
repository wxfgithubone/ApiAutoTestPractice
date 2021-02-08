#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：conftest.py
"""
import sys, os
con_path = os.path.dirname(__file__).replace("Test_case", "") + "Common"
sys.path.append(con_path)
sys.path.append(os.path.dirname(__file__).replace("Test_case", "") + "Params")
import pytest
import platform
from Common.request import HttpRequest
from py._xmlgen import html
from Common.dataBase import MyDb


@pytest.fixture(scope="session", autouse=True)
def user_session():
    print("开始测试")
    MyDb()
    yield
    print("测试结束，删除会话！")
    HttpRequest().close_session()
    MyDb().close_db()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     getattr(report, 'extra', [])
#     report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码
# @pytest.mark.optionalhook
# def pytest_html_report_title(report):
#     report.title = "以下为本次接口自动化测试执行结果"
#
#
# def pytest_configure(config):
#     # 删除原有
#     config._metadata.clear()
#     # 添加自定义
#     config._metadata["项目名称"] = "后台管理系统"
#     config._metadata['接口地址'] = "http://admin.shopmell.com/"
#     config._metadata['Python版本'] = '3.7.4'
#     config._metadata['测试平台'] = platform.platform()
#     config._metadata['第三方库'] = "requests", "pytest-html", "parallel", "xlrd", "PyYaml", "PyTestReport"
#     config._metadata['测试框架'] = "Pytest"
#

# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix):
#     prefix.extend([html.p("所属部门: 产品研发中心")])
#     prefix.extend([html.p("执行人员: autotest")])
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.pop(-1)  # 删除link列 头
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.pop(-1)  # 删除link列
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.pop()
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('用例所属功能'))
#     cells.pop()
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)





