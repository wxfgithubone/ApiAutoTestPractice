#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：read_config.py
"""
import yaml
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Config", "") + "Common")  # Common目录
import traceback
from Common.log import MyLog
from yaml.composer import ComposerError

logger = MyLog()


class YamlHandler:
    """读取yaml配置文件"""
    def __init__(self, file):
        self.file = file

    def read_config(self):
        """配置文件专用"""
        try:
            with open(self.file, mode='r', encoding="utf-8") as f:
                temp = yaml.load_all(f.read(), Loader=yaml.FullLoader)
            dic = {}
            for doc in temp:
                for k, v in doc.items():
                    dic[k] = v
        except BaseException:
            traceback.print_exc()
            logger.error(traceback.format_exc())
        else:
            return dic

    def read(self):
        """读取yaml文件数据"""
        try:
            with open(self.file, encoding='utf-8') as f:
                data = yaml.load(f.read(), Loader=yaml.FullLoader)
        except ComposerError:
            traceback.print_exc()
            logger.error(traceback.format_exc())
        except BaseException:
            traceback.print_exc()
            logger.error(traceback.format_exc())
        else:
            return data

    def write_yaml(self, data, encoding='utf-8'):
        """
        写入
        :param data:
        :param encoding:
        :return:
        """
        try:
            with open(self.file, encoding=encoding, mode='w') as f:
                return yaml.dump(data, stream=f, allow_unicode=True)
        except BaseException:
            traceback.print_exc()
            logger.error(traceback.format_exc())


class ReadIni:
    """读取ini配置文件"""
    pass


yaml_conf_read = os.path.dirname(__file__).replace("\\", "/") + "/config.yaml"


if __name__ == '__main__':
    yaml_data = YamlHandler(yaml_conf_read).read_config()
    print(yaml_data['URL']['QiNiu'])
    # yaml_write = YamlHandler(yaml_write_cookie_path)
    # yaml_write.write_yaml("你好")



