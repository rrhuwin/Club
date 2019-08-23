from django.db import models
from django.contrib.auth.models import AbstractUser

# 继承自AbstractUser
class User(AbstractUser):
    realname = models.CharField(max_length=8, verbose_name="用户名")
    email = models.EmailField(max_length=20,verbose_name='邮箱')
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    qq = models.CharField(max_length=11, verbose_name="QQ号")
    money = models.CharField(verbose_name='金币',max_length=100)


class Category(models.Model):
    """
    新闻类别
    """
    category_name = models.CharField(max_length=12,default=10)

    #  待扩展

    class Meta():
        verbose_name = '新闻类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


class News(models.Model):
    """
    新闻内容
    """
    news_id = models.IntegerField(verbose_name='新闻id',max_length=255)
    s_title = models.CharField(verbose_name='小标题', max_length=255)
    s_ab = models.CharField(verbose_name='小导读', max_length=255)
    img_url = models.CharField(verbose_name='图片地址', max_length=255)
    time = models.CharField(verbose_name='新闻时间', max_length=255)
    title = models.CharField(verbose_name='标题', max_length=255)
    abstrat = models.CharField(verbose_name='导读', max_length=255)
    content = models.TextField(verbose_name='正文', default='')
    category = models.ForeignKey(Category, verbose_name='文章类别')

    # 待更新
    class Meta:
        verbose_name = '新闻内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    # name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    news = models.ForeignKey(News, verbose_name='新闻')
    user = models.ForeignKey(User, verbose_name='用户')

    class Meta:
        verbose_name = '新闻评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]

# 找回密码
class FindPassword(models.Model):
    verify_code = models.CharField(max_length=128, verbose_name="验证码")
    email = models.EmailField(verbose_name="邮箱")
    creat_time = models.DateTimeField(auto_now=True, verbose_name="重置时间")
    status = models.BooleanField(default=False, verbose_name="是否已重置")