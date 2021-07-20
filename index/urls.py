#-*- coding : utf-8 -*-
# coding: utf-8
# @time：2021/7/6 9:35
# @Author：yanl
# @File    : urls.py
# @Software: PyCharm


from django.urls import path, re_path
from . import views
from .views import *
import re

urlpatterns = [
    # path('', views.index,name='index'),
    path('addStaffId', views.addStaffId, name='addStaffId'),
    path('searchIndex/', views.searchIndex, name='searchIndex'),
    path('searchStaff/', views.searchStaff, name='searchStaff'),
    path('searchHis/', views.searchHis, name='searchHis'),

    # 定义首页的路由
    # path('', views.homePage, name='homePage'),



]