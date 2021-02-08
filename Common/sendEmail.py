#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
@Time：    2020/9/17
@IDEName： PyCharm
@FileName：sendEmail.py
"""
import smtplib
from Config.read_config import YamlHandler, yaml_conf_read
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


class SendEmail:

    def __init__(self, html_file, accessory_file):
        """
        HTML正文和附件
        :param html_file: 邮件正文
        :param accessory_file: 附件
        """
        self.html_file = html_file
        self.accessory_file = accessory_file
        self.email_config = YamlHandler(yaml_conf_read).read_config()["Email"]
        # 打开文件，读取
        with open(self.html_file, "rb") as html, open(self.accessory_file, "rb") as accessory:
            self.html_body = html.read()
            self.accessory_body = accessory.read()
        html.close()
        accessory.close()

    def send(self):
        # 设置邮件正文信息
        msg = MIMEMultipart()
        msg["Subject"] = Header(self.email_config["Header"], "utf-8")
        html_body = MIMEText(self.html_body, "html", "utf-8")
        msg.attach(html_body)
        # 定义发件人和收件人
        from_addr = self.email_config["address"]
        to_addr_s = self.email_config["recipients"]
        # 添加附件
        att = MIMEText(self.accessory_body, "html", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att.add_header("Content-Disposition", "attachment", filename=self.accessory_file)
        msg.attach(att)

        # 自定义发件人和收件人信息
        def _format_addr(s):
            addr = parseaddr(s)
            return formataddr(addr)
        msg["From"] = _format_addr(u"{} <{}>".format(self.email_config["username"], from_addr))
        for to_addr in to_addr_s:
            msg["to"] = _format_addr(to_addr)

        # 登录邮箱并发给指定接收人
        smtp = smtplib.SMTP()
        smtp.connect(self.email_config["smtpServer"])
        smtp.login(from_addr, self.email_config["password"])
        smtp.sendmail(from_addr, to_addr_s, msg=msg.as_string())
        smtp.quit()
        print("邮件发送成功！")


if __name__ == '__main__':
    p1 = r"F:\auto_test\admin\pyautoTest\Data\Report\report.html"
    p2 = r"F:\auto_test\admin\pyautoTest\Data\Report\TestApiReport.html"
    send = SendEmail(html_file=p1, accessory_file=p2)
    send.send()
    print(yaml_conf_read)
    ya_co = YamlHandler(yaml_conf_read).read_config()["Email"]
    print(ya_co)







