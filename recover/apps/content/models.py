from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
#
# class User(AbstractUser):
#
#     # 答题系统待开发
class Video(models.Model):
    # 继承自AbstractUser
    titles = models.CharField(max_length=100, verbose_name="视频标题")
    imgurl = models.CharField(max_length=100, verbose_name='图片地址')
    videoid = models.CharField(max_length=101, verbose_name="视频id")

