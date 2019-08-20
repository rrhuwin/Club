# coding=gbk
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from .models import User
from django.contrib.auth.hashers import check_password as auth_check_password  # 检查数据库密文密码和实际明文密码


# 用户注册
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, min_length=3, max_length=12,
                               error_messages={'max_length': '用户名太长了', 'min_length': '用户名太短了', 'required': '用户名不能为空'},
                               widget=widgets.TextInput(attrs={
                                   'class': "form-control", 'id': 'u', 'type': "text", 'placeholder': "用户名*",
                                   'name': "user",
                                   'style': "width: 520px"
                               }))
    email = forms.EmailField(label='邮箱', required=True, error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
                             widget=widgets.EmailInput(
                                 attrs={
                                     'class': "form-control", 'id': 'em', 'type': "email", 'placeholder': "邮箱*",
                                     'name': "email",
                                     'style': "width: 520px"
                                 }
                             ))

    password = forms.CharField(label="密 码2",min_length=6, required=True, error_messages={'min_length': '密码太短了','required': '密码不能为空'},
                               widget=widgets.PasswordInput(attrs={
                                   'class': "form-control", 'id': 'p1', 'type': "password", 'placeholder': "密码*",
                                   'name': "p",
                                   'style': "width: 520px"
                               }))
    password2 = forms.CharField(label="密 码2", required=True, error_messages={'required': '密码不能为空'},
                                widget=widgets.PasswordInput(attrs={
                                    'class': "form-control", 'id': 'p2', 'type': "password", 'placeholder': "确认密码*",
                                    'name': "p2", 'style': "width: 520px"
                                }))
    mobile = forms.CharField(label='手机号', required=True, error_messages={'required': '手机号不能为空'},
                             widget=widgets.TextInput(attrs={
                                 'class': "form-control", 'id': 'pho', 'type': "text", 'placeholder': "手机号*",
                                 'name': "m",
                                 'style': "width: 520px"
                             }))
    mobile_captcha = forms.CharField(label="验证码", required=True, error_messages={'required': '手机验证码不能为空'},
                                     widget=widgets.TextInput(attrs={
                                         'class': "form-control", 'id': 'mc', 'type': "text", 'placeholder': "验证码*",
                                         'name': "mc",
                                         'style': "width: 520px", }))

    # username是否重复django会自动检查，因为它是unique的，所以不需要自己写clean_username

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            if len(data) == 0:
                raise ValidationError("密码不能为空")
            else:
                raise ValidationError("密码不能全是数字")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', required=True, min_length=3, max_length=12,
                               error_messages={'max_length': '用户名太长了', 'min_length': '用户名太短了', 'required': '用户名不能为空'},
                               widget=widgets.TextInput(attrs={
                                   'class': "form-control", 'id': 'u', 'type': "text", 'placeholder': "用户名*",
                                   'name': "user",
                                   'style': "width: 520px"
                               }))

    password = forms.CharField(label="密 码",required=True,error_messages={ 'required': '密码不能为空'},widget=widgets.PasswordInput(
                                   attrs={'class': "form-control", 'style': "width: 520px", "placeholder": "请输入密码*",
                                          'type': "password", 'id': 'p5', }))
    captcha = forms.CharField(label="验证码",required=True,error_messages={'required': '验证码不能为空'}, widget=widgets.TextInput(
        attrs={'class': "form-control", "placeholder": "验证码*", "onblur": "check_captcha()", 'style': "width: 520px",
               'id': 'cat', }))

    def check_password(self):
        # print('check password')
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            user = User.objects.get(username=username)

            return user, auth_check_password(password, user.password)
        except:
            return None, False
    #
    # def clean_username(self):
    #     # print('hahaha')
    #     # print(self.cleaned_data.get("username"))
    #     ret = User.objects.filter(username=self.cleaned_data.get("username"))
    #     if ret:
    #         return self.cleaned_data.get("username")
    #     else:
    #         raise ValidationError("用户名或密码不正确")
