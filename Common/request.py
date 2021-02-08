#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：request.py
"""
import sys
import os
import requests
import json
import urllib3
import traceback
from json import JSONDecodeError
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__).replace("Common", "") + "Params")
from Common.log import MyLog

logger = MyLog()


class HttpRequest:

    def __init__(self):
        self.session = requests.session()
        self.warnings = urllib3.disable_warnings()

    def send_request(self, method, url, params_type="JSON", data=None, **kwargs):
        """
        按照项目对requests二次封装
        :param method: 请求方法
        :param url: 请求地址
        :param params_type: 请求参数类型，默认为JSON
        :param data: 参数
        :param kwargs: 不限个数的键值对参数
        :return:
        """
        method = method.upper()
        params_type = params_type.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)  # 字符串转字典
                logger.info("转换为字典")
                print("转换为字典")
            except TypeError or JSONDecodeError:
                data = eval(data)  # loads失败就按传入的字符串格式转换
                logger.info("loads失败")
                print("loads失败")
        if "GET" == method:
            try:
                response = self.session.request(method=method, url=url, params=data, verify=False, **kwargs)
            except BaseException as err:
                logger.error(err)
            else:
                logger.info(
                    f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                    f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                    f"耗时：{response.elapsed.total_seconds()}s")
                return response
        elif "POST" == method:
            if params_type == "FROM":
                try:
                    response = self.session.request(method=method, url=url, data=data, verify=False, **kwargs)
                except BaseException as err:
                    logger.error(err)
                else:
                    try:
                        logger.info(
                            f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                            f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                            f"耗时：{response.elapsed.total_seconds()}s")
                    except KeyError:
                        pass
                    return response
            elif params_type == "JSON":
                try:
                    response = self.session.request(method=method, url=url, json=data, verify=False, **kwargs)
                except BaseException as err:
                    logger.error(err)
                else:
                    logger.info(
                        f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                        f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                        f"耗时：{response.elapsed.total_seconds()}s")
                    return response
        elif "PUT" == method:
            if params_type == "JSON":
                try:
                    response = self.session.request(method=method, url=url, json=data, verify=False, **kwargs)
                except BaseException as err:
                    logger.error(err)
                else:
                    logger.info(
                        f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                        f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                        f"耗时：{response.elapsed.total_seconds()}s")
                    return response
            elif params_type == "FROM":
                try:
                    response = self.session.request(method=method, url=url, data=data, verify=False, **kwargs)
                except BaseException as err:
                    logger.error(err)
                else:
                    logger.info(
                        f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                        f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                        f"耗时：{response.elapsed.total_seconds()}s")
                    return response
        elif "DELETE" == method:
            try:
                response = self.session.request(method=method, url=url, params=data, verify=False, **kwargs)
            except BaseException as err:
                logger.error(err)
            else:
                logger.info(
                    f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                    f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                    f"耗时：{response.elapsed.total_seconds()}s")
                return response
        elif "PUT" == method:
            try:
                response = self.session.request(method=method, url=url, params=data, verify=False, **kwargs)
            except BaseException as err:
                logger.error(err)
            else:
                logger.info(
                    f"请求路径：{response.request.url}\n请求头：{response.request.headers}\n请求体：{response.request.body}\n"
                    f"响应码：HTTP：{response.status_code} 自定义：{response.json()['code']};"
                    f"耗时：{response.elapsed.total_seconds()}s")
                return response
        else:
            logger.warning("使用{}方法请重新定义".format(method) + traceback.format_exc())
            raise ValueError("{} 该请求方法未定义！！！".format(method))

    def __call__(self, method, url, params_type="json", data=None, **kwargs):
        return self.send_request(method=method, url=url, params_type=params_type, data=data, **kwargs)

    def close_session(self):
        """删除会话"""
        self.session.close()
        try:
            logger.info(self.session.cookies)
            del self.session.cookies
        except BaseException as err:
            traceback.print_exc(err)
            logger.error(traceback.format_exc(err))


request = HttpRequest()


if __name__ == '__main__':
    ...
