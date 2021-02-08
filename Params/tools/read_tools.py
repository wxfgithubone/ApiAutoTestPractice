#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：read_tools.py
"""
import xlrd
import os
import yaml
import json
from json import JSONDecodeError


class ReadExcel:

    def __init__(self, file_path, sheet_name):
        """
        填写文件路径和表单下标，从第几行开始读取以及到第几行结束
        :param file_path: 文件路径
        :param sheet_name: excel里的表单
        """
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.workbook = xlrd.open_workbook(self.file_path, formatting_info=True)
        self.work_sheet = self.workbook.sheet_by_name(self.sheet_name)

    def auto_excel_read(self, case_name, title_col=2, priority_col=3, describe_col=4, url_col=5,
                        method_col=7, body_col=None, dynamic_col=None, test_step_col=11, expected_col=12):
        """
        :param case_name: 用例名称
        :param title_col: 用例标题
        :param priority_col：优先级
        :param describe_col: 用例描述
        :param url_col: 请求路径列
        :param method_col: 请求方法列
        :param body_col: 请求参数列
        :param dynamic_col: 动态参数
        :param test_step_col：测试步骤
        :param expected_col: 预期结果列
        :return: list
        """
        if body_col and dynamic_col:
            data_list = []
            idx = 0
            for one in self.work_sheet.col_values(1):
                if case_name in one:
                    data_list.append((
                        self.work_sheet.cell(idx, title_col).value,
                        self.work_sheet.cell(idx, priority_col).value,
                        self.work_sheet.cell(idx, describe_col).value,
                        self.work_sheet.cell(idx, url_col).value,
                        self.work_sheet.cell(idx, method_col).value,
                        self.work_sheet.cell(idx, body_col).value,
                        self.work_sheet.cell(idx, dynamic_col).value,
                        self.work_sheet.cell(idx, test_step_col).value,
                        self.work_sheet.cell(idx, expected_col).value
                    ))
                idx += 1
            return data_list
        elif body_col:
            data_list = []
            idx = 0
            for one in self.work_sheet.col_values(1):
                if case_name in one:
                    data_list.append((
                        self.work_sheet.cell(idx, title_col).value,
                        self.work_sheet.cell(idx, priority_col).value,
                        self.work_sheet.cell(idx, describe_col).value,
                        self.work_sheet.cell(idx, url_col).value,
                        self.work_sheet.cell(idx, method_col).value,
                        self.work_sheet.cell(idx, body_col).value,
                        self.work_sheet.cell(idx, test_step_col).value,
                        self.work_sheet.cell(idx, expected_col).value
                    ))
                idx += 1
            return data_list
        elif dynamic_col:
            data_list = []
            idx = 0
            for one in self.work_sheet.col_values(1):
                if case_name in one:
                    data_list.append((
                        self.work_sheet.cell(idx, title_col).value,
                        self.work_sheet.cell(idx, priority_col).value,
                        self.work_sheet.cell(idx, describe_col).value,
                        self.work_sheet.cell(idx, url_col).value,
                        self.work_sheet.cell(idx, method_col).value,
                        self.work_sheet.cell(idx, dynamic_col).value,
                        self.work_sheet.cell(idx, test_step_col).value,
                        self.work_sheet.cell(idx, expected_col).value
                    ))
                idx += 1
            return data_list
        elif not body_col and not dynamic_col:
            data_list = []
            idx = 0
            for one in self.work_sheet.col_values(1):
                if case_name in one:
                    data_list.append((
                        self.work_sheet.cell(idx, title_col).value,
                        self.work_sheet.cell(idx, priority_col).value,
                        self.work_sheet.cell(idx, describe_col).value,
                        self.work_sheet.cell(idx, url_col).value,
                        self.work_sheet.cell(idx, method_col).value,
                        self.work_sheet.cell(idx, test_step_col).value,
                        self.work_sheet.cell(idx, expected_col).value
                    ))
                idx += 1
            return data_list
        else:
            data_list = []
            idx = 0
            for one in self.work_sheet.col_values(1):
                if case_name in one:
                    data_list.append((
                        self.work_sheet.cell(idx, title_col).value,
                        self.work_sheet.cell(idx, priority_col).value,
                        self.work_sheet.cell(idx, describe_col).value,
                        self.work_sheet.cell(idx, url_col).value,
                        self.work_sheet.cell(idx, method_col).value,
                        self.work_sheet.cell(idx, test_step_col).value,
                        self.work_sheet.cell(idx, expected_col).value
                    ))
                idx += 1
            return data_list

    def auto_dynamic(self, case_name, dynamic_col=10):
        """Case专用，读取前置参数"""
        data_list = []
        idx = 0
        for one in self.work_sheet.col_values(1):
            if case_name in one:
                data_list.append((
                    self.work_sheet.cell(idx, dynamic_col).value))
            idx += 1
        return data_list

    def lead_params(self):
        """conftest.py文件专用，读取前置参数"""
        all_content = []
        for exl in range(1, self.work_sheet.nrows):
            if self.work_sheet.cell_value(exl, 10) == '':
                pass
            else:
                all_content.append(self.work_sheet.cell_value(exl, 10))
        return all_content


# 全局路径
admin_path = f'{os.path.dirname(__file__)}excel/admin接口测试用例.xls'.replace("tools", "")
API_admin_path = f'{os.path.dirname(__file__)}excel/admin_API_case.xls'.replace("tools", "")


class ReadYaml(object):
    """读取yaml用例"""
    def __init__(self, file):
        self.file = file

    def read_yaml(self):
        """读取全部"""
        with open(self.file, encoding="utf-8") as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def get_yaml_data(self):
        """定制化读取"""
        with open(self.file, encoding='utf-8') as f:
            res = yaml.load(f.read(), Loader=yaml.FullLoader)
            res_list = []
            for one in res:
                res_list.append((json.dumps(one, ensure_ascii=False)))
            return res_list


def switch_data(data):
    """数据转换"""
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except TypeError or JSONDecodeError:
            data = eval(data)
        return data
    else:
        raise ValueError("请填写字符串类型的参数")


if __name__ == '__main__':
    api_data = ReadExcel(API_admin_path, "commodity_manage")
    auto_data = api_data.lead_params()
    print(auto_data)
    dc = {}
    for i in auto_data:
        data = switch_data(i)
        for k, v in data.items():
            dc[k] = v
    print(dc)




