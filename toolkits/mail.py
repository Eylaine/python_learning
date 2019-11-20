# -*- coding: utf-8 -*-
# Time   : 2019/11/20 3:06 下午
# Author : Eylaine
# File   : mail.py

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from toolkits.logger import record_log, logger


class Email:

    email_config = Config.get_email_config()

    def __init__(self, mail_info, _html=False, _icon=None):
        self.mail_info = mail_info
        self.html = _html
        self.icon = _icon

    @record_log
    def send_email(self):
        """发送邮件"""
        logger.info(f"mail_info: {self.mail_info}")

        sender = self.email_config["sender"]
        password = self.email_config["password"]
        server = self._connect(sender, password)

        to = self.email_config["to"]
        # cc = self.email_config["cc"]
        content = self.mail_info["content"]

        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = to
        # message["Cc"] = cc
        message["Subject"] = self.mail_info["subject"]

        if self.html or self.icon:
            if self.html:
                html = self.parse_html(content)
                message.attach(html)
            if self.icon:
                icon = self.parse_icon()
                message.attach(icon)
        else:
            text = self.parse_text(content)
            message.attach(text)

        to_addr = to.split(";")
        # to_addr = to.split(";") + cc.split(";")
        server.sendmail(sender, to_addr, message.as_string())

    @staticmethod
    def parse_html(content):
        """发送html格式邮件"""
        message = MIMEText(content, _subtype="html", _charset="utf8")
        return message

    @staticmethod
    def parse_icon():
        """发送带图片的邮件, picture text"""
        icon_path = ""
        with open(icon_path, "rb") as icon:
            img = MIMEImage(icon.read())
        img.add_header("Content-ID", "icon")

        return img

    @staticmethod
    def parse_text(content):
        """发送纯文本邮件"""
        return MIMEText(content)

    @staticmethod
    def _connect(username, password):
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(username, password)

        return server
