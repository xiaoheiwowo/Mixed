# !/usr/bin/python3
# coding: utf-8

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr
from email.utils import formataddr


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))


from_email = "liupengyu1556@126.com"
from_email_pwd = "tjurrr6ktq"
to_email = "liupengyu1556@163.com"
smtp_server = "smtp.126.com"

msg = MIMEText("<html><body><h3>hello</h3><p>hello, send by python</p></body></html>", "html", "utf-8")
msg["From"] = format_addr("%s" % (from_email))
msg["To"] = format_addr("%s" % (to_email))
msg["Subject"] = Header("python email", "utf-8").encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_email, from_email_pwd)
server.sendmail(from_email, [to_email], msg.as_string())
