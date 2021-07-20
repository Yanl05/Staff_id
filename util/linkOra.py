#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/7/19 9:23
# @Author：yanl
# @File    : linkOra.py
# @Software: PyCharm
"""
连接oracle 数据库
"""
# 避免编码问题带来的乱码
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# 连接数据库
from sqlalchemy import create_engine
from util import config

def linkOra():
    engine = create_engine('oracle+cx_oracle://{name}:{pwd}@172.16.20.246:1521/zyyfsyy'.format(name=config.ora_name, pwd=config.ora_pwd))
    return engine