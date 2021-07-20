from django.test import TestCase

# Create your tests here.
"""
在Python脚本中调用Django环境
"""
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Staff_id.settings")
    import django

    django.setup()

    from index import models

    stf = models.StaffInfo.objects.filter(name='123', keshi='123').first()
    print(stf.name)