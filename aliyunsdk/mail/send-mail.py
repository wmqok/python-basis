#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtpdm.aliyun.com"  #设置服务器
mail_user="xxx@xxx.com"    #用户名
mail_pass="xxxxxxxxxxx"   #口令 
 
 
sender = 'xxx@xxx.com'
receivers = ['xxx@xxx.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('邮件内容xxxxxxxxxxx', 'plain', 'utf-8')
message['From'] = Header("xxx@xxx.com", 'utf-8')
message['To'] =  Header("xxx@xxx.com", 'utf-8')
 
subject = 'Python SMTP'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")