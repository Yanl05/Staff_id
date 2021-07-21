from django.db import models

# Create your models here.
class User(models.Model):
    staffid = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"