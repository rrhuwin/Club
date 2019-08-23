from django.db import models
from apps.count.models import User
from ckeditor.fields import RichTextField
# 含文件上传
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Category(models.Model):
    """分类"""
    name = models.CharField("分类名称", max_length=64)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"


class Questions(models.Model):
    """题库"""
    category = models.ForeignKey(Category, verbose_name="所属分类", null=True)
    title = models.CharField(verbose_name="题目", unique=True, max_length=255)
    content = models.CharField(verbose_name="题目解析", null=True, max_length=100)
    answer = models.CharField(verbose_name="题目答案", null=True, max_length=100)
    choose_A = models.CharField(verbose_name='A选项', max_length=100)
    choose_B = models.CharField(verbose_name='B选项', max_length=100)
    choose_C = models.CharField(verbose_name='C选项', max_length=100)
    choose_D = models.CharField(verbose_name='D选项', max_length=100)
    choose_E = models.CharField(verbose_name='E选项', max_length=100)


    class Meta:
        verbose_name = "题库"
        verbose_name_plural = verbose_name
        permissions = (
            ('can_change_question', "可以修改题目信息"),
            ('can_add_question', "可以添加题目信息"),
        )

    def __str__(self):
        return f"{self.id}:{self.title}"


class QuestionsCollection(models.Model):
    """收藏问题"""
    question = models.ForeignKey(Questions, verbose_name="问题")
    user = models.ForeignKey(User, verbose_name="收藏者" )
    create_time = models.DateTimeField("收藏/取消时间", auto_now=True)
    # True表示收藏 ,False表示未收藏
    status = models.BooleanField("收藏状态", default=True)

    class Meta:
        verbose_name = "收藏记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status: ret="收藏"
        else: ret="取消收藏"
        return f"{self.user}:{ret}:{self.question.title}"


class Questionsliker(models.Model):
    """喜欢问题"""
    question = models.ForeignKey(Questions, verbose_name="问题" )
    user = models.ForeignKey(User, verbose_name="喜欢者")
    create_time = models.DateTimeField("喜欢/取消时间", auto_now=True)
    # True表示收藏 ,False表示未收藏
    status = models.BooleanField("喜欢状态", default=True)

    class Meta:
        verbose_name = "喜欢记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status: ret="喜欢"
        else: ret="取消喜欢"
        return f"{self.user}:{ret}:{self.question.title}"