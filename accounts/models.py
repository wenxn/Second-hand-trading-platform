from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserInfo(models.Model):
    """
    用户
    """
    nid = models.BigAutoField(primary_key=True)
    student_id = models.IntegerField(verbose_name='学号', null=True, blank=True)
    username = models.CharField(verbose_name='姓名', max_length=32,unique=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    Institute = models.CharField(verbose_name='学院', max_length=32, null=True, blank=True)
    introduce = models.CharField(verbose_name='个人介绍', max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', unique=True, null=True, blank=True)
    latest_login_time = models.DateTimeField(verbose_name='最近登录时间', null=True, blank=True)
    photo = models.ImageField(verbose_name='头像', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = '用户'
    def __str__(self):
        return self.username