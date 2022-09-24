from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    """
    基本用户表
    """
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='手机号码', help_text='手机号码')
    desc = models.TextField(null=True, blank=True, verbose_name='账号描述', help_text='账号描述')

    class Meta:
        db_table = 'user_base'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
