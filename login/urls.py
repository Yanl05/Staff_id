# -*- coding: UTF-8 -*-

"""
# @Time    : 2021-07-20 21:43
# @Author  : yanlei
# @FileName: urls.py
"""
from django.urls import path, re_path
from . import views
from .views import *
import re

urlpatterns = [
    path('', views.login,name='login'),
    path('login/', views.login, name='login'),

    # 定义首页的路由
    # path('', views.homePage, name='homePage'),



]