from django.shortcuts import render,redirect,reverse
from login import models
# Create your views here.

def login(request):
    if request.method == "POST":
        staffid = request.POST.get('staffid', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        print(staffid,password)
        if staffid and password:  # 确保用户名和密码都不为空
            staffid = staffid.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                staffid = models.User.objects.get(staffid=staffid)
                if staffid.password == password:
                    return redirect(reverse('index:searchIndex'))
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')


