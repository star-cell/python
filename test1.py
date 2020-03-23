#!/usr/bin/env python3
#coding: utf-8
import sys
import os
import time
import smtplib
from email.mime.text import MIMEText

sender = 'limengxing@zhidaoauto.com'
smtpserver = 'smtp.exmail.qq.com'
username = 'limengxing@zhidaoauto.com'
password = 'Zhidao@2018'


subject = 'python email test'
receiver = 'limengxing@zhidaoauto.com'
content='test111111'

msg = MIMEText(content,'html','utf-8')

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
##smtp.sendmail(sender, receiver, msg.as_string())
##smtp.quit()

help(smtplib.SMTP)
print(type(msg))