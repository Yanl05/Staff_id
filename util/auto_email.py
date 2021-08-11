# -*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/1/28 15:05
# @Author：yanl
# @File    : auto_email.py
# @Software: PyCharm

import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

Current_cwd = os.path.abspath(os.path.dirname(__file__))
LogDir = Current_cwd + r'\log'
LogDirMailToday = LogDir + '\\' + time.strftime('%Y%m%d')  # 以日期创建目录

Mail_List_File = Current_cwd + r'\etc\\Mail_list.ini'
ZIPFILE = os.path.basename(LogDirMailToday) + '1.zip'

# FILENAME = 'C:/Users/Administrator/Desktop/历史文档数据/白草妇净2020/0801-1231/巨龙门诊.csv'
SMTP_Sever = 'smtp.qq.com'

'''
Send_Mail()
发送邮件函数
'''


def Send_Mail(Mail_User, Mail_Pwd, Mail_To, data):
    # Mail_List = file(Mail_List_File)#邮件地址列表
    # Mail_To   = []
    # for list in Mail_List:#读取邮件列表文件
    #     Mail_To.extend(list.strip().split(','))
    # Mail_List.close()
    msg = MIMEMultipart()
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    Subject = '新增工号工单'
    Content = '医务部已提交新工号，请查看'  # + str(success_count)  + ' 巡检失败: ' + str(failed_count)
    detail = '姓名：' + data['name'] + '<br>'+ '  科室： ' + data['keshi'] + '<br>'+ ' 职称： ' + data['zhicheng'] + '<br>'+ ' 岗位： ' + data['gangwei']
    Content = Content + '<br>' + detail + '<br>' + "-----------" + '<br>' + "这是一份自动邮件，请不要回复！！"
    msg["Subject"] = Subject  # 邮件标题
    msg["From"] = Mail_User
    msg["To"] = Mail_To
    msgContent = MIMEText(Content, 'html', 'utf-8')  # 邮件内容
    msgContent["Accept-Language"] = "zh-CN"
    msgContent["Accept-Charset"] = "ISO-8859-1,utf-8"
    msg.attach(msgContent)

    s = smtplib.SMTP_SSL(SMTP_Sever, '465')
    s.ehlo()
    try:
        s.login(Mail_User, Mail_Pwd)
        s.sendmail(Mail_User, Mail_To, msg.as_string())  # 发送邮件
        s.close()
        print('邮件发送成功！')
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    Send_Mail('756593069@qq.com', 'bjyxsqgrzrrxbgab', '756593069@qq.com')
