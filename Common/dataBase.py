#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：dataBase.py
"""
import os
import sys
import pymysql
import traceback
sys.path.append(os.path.abspath(os.path.dirname(__file__)).replace("Common", "") + "Config")  # Config目录
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 当前目录
from Common.log import MyLog
from pymysql.err import MySQLError
from Config.read_config import YamlHandler, yaml_conf_read

logger = MyLog()
db_config = YamlHandler(yaml_conf_read).read_config()["MySQL"]


class MyDb(object):

    def __init__(self, host=db_config["host"], port=db_config["port"], user=db_config["user"],
                 password=db_config["password"], db_name=db_config["db_name"]):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name)
            self.cursor = self.conn.cursor()
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库连接的异常：" + traceback.format_exc())
        else:
            print("数据库连接正常")
            logger.info("数据库连接正常")

    def slt_all_data(self, table):
        """查询所有数据"""
        try:
            self.cursor.execute(f"select * from {table}")
            all_data = self.cursor.fetchall()
            logger.info("查询数据：" + str(f"select * from {table}"))
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库执行查询语句的异常：" + traceback.format_exc())
        else:
            return all_data

    def slt_one_data(self, table, condition):
        """查询一条数据"""
        try:
            self.cursor.execute(f"select * from {table} where {condition}")
            one_data = self.cursor.fetchone()
            logger.info("查询数据：" + str(f"select * from {table} where {condition}"))
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库查询语句的异常：" + traceback.format_exc())
        else:
            return one_data

    def del_data(self, table, condition):
        """删除一条数据"""
        try:
            self.cursor.execute(f"delete from {table} where {condition}")
            self.conn.commit()
            logger.info("删除数据：" + str(f"delete from {table} where {condition}"))
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库删除语句的异常：" + traceback.format_exc())
            self.conn.rollback()  # 回滚当前事务

    def upd_date(self, table, obj, condition):
        """更新一条数据"""
        try:
            self.cursor.execute(f"update {table} set {obj} where {condition}")
            self.conn.commit()
            logger.info("更新数据：" + str(f"update {table} set {obj} where {condition}"))
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库修改语句的异常：" + traceback.format_exc())
            self.conn.rollback()

    def ins_data(self, table, *args):
        """插入一条数据"""
        try:
            self.cursor.execute(f"insert into {table}{args} values {args}")
            self.conn.commit()
            logger.info("插入数据：" + str(f"insert into {table}{args} values {args}"))
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库插入语句的异常：" + traceback.format_exc())
            self.conn.rollback()

    def close_db(self):
        try:
            self.cursor.close()
            self.conn.close()
        except MySQLError:
            traceback.print_exc()
            logger.error("数据库关闭连接的错误：" + traceback.format_exc())
        else:
            print("关闭数据库连接")
            logger.info("关闭数据库连接")


if __name__ == '__main__':
    db = MyDb()
    print(db_config)







