from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import StaffInfo
from index import models
import json
import os
from util import auto_email
# Create your views here.

from functools import wraps


def check_login(f):
    @wraps(f)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        print(next_url)
        if request.session.get("is_login") == "1":
            return f(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))

    return inner


@check_login
def index(request):
    return render(request, 'index.html')


@check_login
def addStaffId(request):
    if request.method == 'POST':
        """
        姓名、职称、科室、岗位
        """
        name = request.POST['name']
        zhicheng = request.POST['zhicheng']
        keshi = request.POST['keshi']
        gangwei = request.POST['gangwei']
        """
        抗生素、毒麻、放射药品、一类精神药品、二类精神、线控药品、门诊权限、备注
        """
        kss = request.POST.get('kss')
        duma = request.POST.get('duma')
        fsyp = request.POST.get('fsyp')
        yljs = request.POST.get('yljs')
        eljs = request.POST.get('eljs')
        xkyp = request.POST.get('xkyp')
        mzqx = request.POST.get('mzqx')
        bz = request.POST.get('bz')

        data = {'name': name,
                'zhicheng': zhicheng,
                'keshi': keshi,
                'gangwei': gangwei,
                'kss': kss,
                'duma': duma,
                'fsyp': fsyp,
                'yljs': yljs,
                'eljs': eljs,
                'xkyp': xkyp,
                'mzqx': mzqx,
                'bz': bz}
        # 空值替换
        for k, v in data.items():
            if v is None:
                data[k] = 999

        print(name, zhicheng, keshi, gangwei, kss, duma, fsyp, yljs, eljs, xkyp, mzqx, bz)

        staff = models.StaffInfo.objects.create(**data)
        if staff:
            # 新增成功，则向邮箱发送信息
            data = {'name': name, 'zhicheng': zhicheng, 'keshi': keshi, 'gangwei': gangwei}
            auto_email.Send_Mail(config.Mail_User, config.Mail_Pwd, config.Mail_To, data)

            return render(request, 'success.html')
        else:
            return render(request, 'failtoadd.html')
    else:
        return render(request, 'addStaffId.html')


@check_login
def searchIndex(request):
    return render(request, 'serachHistory.html')


@check_login
def searchStaff(request):
    name = request.POST.get('name')
    keshi = request.POST.get('keshi')
    print('检索条件：', name, keshi)

    stf = StaffInfo.objects.filter(name=name, keshi=keshi).first()
    print(stf.name)
    print("name=", stf.name)
    data = {'name': stf.name,
            'zhicheng': stf.zhicheng,
            'keshi': stf.keshi,
            'gangwei': stf.gangwei,
            'kss': stf.kss,
            'duma': stf.duma,
            'fsyp': stf.fsyp,
            'yljs': stf.yljs,
            'eljs': stf.eljs,
            'xkyp': stf.xkyp,
            'mzqx': stf.mzqx,
            'bz': stf.bz
            }
    # 空值替换
    for k, v in data.items():
        # print(k,v)
        if v == '999':
            print(data[k])
            data[k] = None
            print(data[k])
    print(data)
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")


@check_login
def searchProgress(request):
    """:arg
    查询工号开通进度
    """
    if request.method == 'GET':
        return render(request, 'serachProgress.html')
    else:
        staff_list = models.StaffInfo.objects.all()[:10]
        retset = []
        tmp = {}
        for i in staff_list:
            print(i)
            tmp['name'] = i.name
            tmp['keshi'] = i.keshi
            tmp['zhicheng'] = i.zhicheng
            tmp['gangwei'] = i.gangwei
            if i.jindu == '待开通':
                tmp['jindu'] = i.jindu
            else:
                tmp['jindu'] = '工号： ' + i.jindu
            print(tmp)
            retset.append(tmp)
            tmp = {}
        data = {'status': 1, 'data': retset}
        data = json.dumps(data)

        return HttpResponse(data, content_type="application/json")


@check_login
def updateStaff(request):
    """:arg
    更新数据库中的  进度信息
    """
    name = request.POST.get('name')
    keshi = request.POST.get('keshi')


from util import config, linkOra


@check_login
def searchHis(request):
    if request.method == 'GET':
        return render(request, 'serachHis.html')

    name = request.POST.get('name')
    keshi = request.POST.get('keshi')
    print('检索条件：', name, keshi)
    # 获取sql
    sqlfile = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'sql\查询权限.sql')

    stf = StaffInfo.objects.filter(name=name, keshi=keshi).first()
    print(stf.name)
    print("name=", stf.name)
    data = {'name': stf.name,
            'zhicheng': stf.zhicheng,
            'keshi': stf.keshi,
            'gangwei': stf.gangwei,
            'kss': stf.kss,
            'duma': stf.duma,
            'fsyp': stf.fsyp,
            'yljs': stf.yljs,
            'eljs': stf.eljs,
            'xkyp': stf.xkyp,
            'mzqx': stf.mzqx,
            'bz': stf.bz
            }
    # 空值替换
    for k, v in data.items():
        # print(k,v)
        if v == '999':
            print(data[k])
            data[k] = None
            print(data[k])
    print(data)
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")
