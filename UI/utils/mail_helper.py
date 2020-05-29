# -*- coding: utf-8 -*-

# 发送邮箱服务器
import smtplib
from configparser import ConfigParser
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.basepath_helper import config_path

#mail_host = 'smtp.exmail.qq.com'
mail_host = 'smtp.qq.com'

# 发送邮箱用户名/密码
mail_user = '1925719012@qq.com'
# 设置授权码（即客户端的密码）
mail_pass = 'cfqvpgqildfvegee'

# 发送邮箱
sender = '1925719012@qq.com'

# 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
to_list1 = ['Alice.Tang@an-chen.com']
to_list2 = ['Alice.Tang@an-chen.com','Shelly Chen <shelly.chen@redriver.com>','Yan.Liu <Yan.Liu@an-chen.com>']

config = ConfigParser()
file_path = config_path + 'config.ini'
config.read(file_path)

url = config.get("testServer", "URL")


def send_mail(file_new):
    # 设置totest的值
    totest = 1
    f = open(file_new, 'rb')              # 打开文件
    mail_body = f.read()                  # 读取文件内容
    f.close()                             # 关闭文件

    # 编写 HTML类型的邮件正文
    msg = MIMEMultipart()
    msg['Subject'] = Header(u"Automation Test Report(" + url + ")", 'utf-8')
    msg["From"] = "{}".format(sender)
    # 判断totest=1  接收方为to_list1中的收件人  非1为to_list2中的收件人
    if totest == 1:
        to_list = to_list1
    else:
        to_list = to_list2
    msg["To"] = ",".join(to_list)

    # 邮件内容
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(text)

    # 发送附件
    att = MIMEApplication(open(file_new, 'rb').read())
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', "report.html"))
    msg.attach(att)

    # 连接发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)              # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)                     # 登录验证
        smtpObj.sendmail(sender, to_list, msg.as_string())      # 发送
        # print("mail has been send successfully.")
        print("email has been sent successfull,please check")
    except smtplib.SMTPException as e:
        print(e)
        print('email sent failure！！')
