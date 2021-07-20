from django.db import models

# Create your models here.
class StaffInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    zhicheng = models.CharField(max_length=20)
    keshi = models.CharField(max_length=20)
    gangwei = models.CharField(max_length=20)

    kss = models.IntegerField()
    duma = models.CharField(max_length=20)
    fsyp = models.CharField(max_length=20)
    yljs = models.CharField(max_length=20)
    eljs = models.CharField(max_length=20)
    xkyp = models.CharField(max_length=20)
    mzqx = models.CharField(max_length=20)
    bz = models.CharField(max_length=200)
