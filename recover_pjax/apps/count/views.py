from .forms import RegisterForm, LoginForm
from .models import User, FindPassword,News
from apps.questions.models import *
from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.hashers import make_password
from libs import sms, patcha
import base64
from io import BytesIO
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import time
from django.http import JsonResponse
import random
import string
from django.core.mail import send_mail
# Create your views here.
yanzhenma = []
start = time.time()

# 注册
def register(request):
    if request.method == "GET":
        form = RegisterForm()
        # 如果已登录，则直接跳转到index页面
        # request.user 表示的是当前登录的用户对象,没有登录 `匿名用户`
        cc = News.objects.filter(category_id=5)
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        lform = LoginForm()
        # 设置下一跳转地址
        # request.session["next"] = request.GET.get('next', reverse('index'))
        return render(request, "login.html", {"l_form": lform, "form": form,'cc':cc})
    # Ajax提交表单
    else:
        from django.core.cache import cache
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                email = form.cleaned_data['email']
                mobile = form.cleaned_data["mobile"]
                global yanzhenma, nowtime

                mobile_captcha = form.cleaned_data["mobile_captcha"]
                mobile_captcha_reids = yanzhenma[0]
                nowtime = time.time()

                if mobile_captcha == mobile_captcha_reids:
                    user = User.objects.create(username=username, password=make_password(password), email=email,
                                               mobile=mobile)
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    yanzhenma = []
                    # logger.debug(f"新用户{user}注册成功！")
                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                    else:
                        pass
                else:
                    # 验证码错误
                    if nowtime - start >= 60:
                        yanzhenma = []
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
        return JsonResponse(ret)

# 登录
def login(request):
    if request.method == "GET":
        lform = LoginForm()
        cc = News.objects.filter(category_id=5)

        # 设置下一跳转地址
        # request.session["next"] = request.GET.get('next', reverse('index'))
        return render(request, "login.html", {"l_form": lform,'cc':cc })
    else:
        res = {"status": 0, "msg": ""}
        if request.is_ajax():
            form = LoginForm(request.POST)
            # print(form.cleaned_data['username'])
            if form.is_valid():
                username = form.cleaned_data["username"]
                request.session['user'] = username
                captcha = form.cleaned_data["captcha"]
                session_captcha_code = request.session.get("captcha_code", "")
                # 验证码一致
                if captcha.lower() == session_captcha_code.lower():
                    user, flag = form.check_password()
                    # print(request.session.get('user'))
                    # user = auth.authenticate(username=username, password=password)
                    if flag and user and user.is_active:
                        auth.login(request, user)
                        res['status'] = 200
                        res['msg'] = '登录成功'
                    else:
                        res['status'] = 403
                        res['msg'] = '用户名密码错误'
            else:
                res['status'] = 402
                res['msg'] = form.errors
            return JsonResponse(res)


@login_required
def loginout(request):
    auth_logout(request)
    return redirect(reverse('index'))


# 忘记密码
# def change(request):
#     return render(request, 'chagepass.html')


class Change(View):
    def get(self, request):
        return render(request, "chagepass.html")

    def post(self, request):
        email = request.POST.get("email")
        if email and User.objects.filter(email=email):
            verify_code = "".join(random.choices(string.ascii_lowercase + string.digits, k=128))
            url = f"{request.scheme}://{request.META['HTTP_HOST']}/count/newpass/{verify_code}?email={email}"
            ret = FindPassword.objects.get_or_create(email=email)
            # (<FindPassword: FindPassword object>, True)
            ret[0].verify_code = verify_code
            ret[0].status = False
            ret[0].save()

            send_mail('注册用户验证信息', url, None, [email])
            msg = {'code': 200, 'msg': "邮件发送成功，请登录邮箱查看！"}
            return JsonResponse(msg)
        else:
            msg = {'code': 404, 'msg': "输入的邮箱不存在！"}
            return JsonResponse(msg)


# 重置密码
class PasswordReset(View):
    def get(self, request, verify_code):
        """
        判断dangqurl是否有效（1.时间）
        :param request:
        :param verify_code:
        :return:
        """
        import datetime
        # 获取utcnow是临时区的时间
        email = request.GET.get("email")
        # verify_code=request.GET.get('')
        url = f"?email={email}"
        create_time_newer = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        # 邮箱、verify_code、status=False、时间近30分钟
        find_password = FindPassword.objects.filter(status=False, verify_code=verify_code, email=email,
                                                    creat_time__gte=create_time_newer)
        # great_then_equal, lte, lt, gt
        if verify_code and find_password:
            return render(request, "newpass.html", {'urls': url})
        else:
            return HttpResponse("链接失效或有误")

    def post(self, request, verify_code):
        import datetime
        create_time_newer = datetime.datetime.utcnow() - datetime.timedelta(minutes=30)
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if len(password1) == 0 or len(password2) == 0:
            msg = {'code': 401, 'msg': '密码不能为空'}
            return JsonResponse(msg)
        if password2 == password1:
            try:
                find_password = FindPassword.objects.get(status=False, verify_code=verify_code,
                                                         creat_time__gte=create_time_newer)
                user = User.objects.get(email=find_password.email)
                user.set_password(password1)
                user.save()
                msg = {'code': 200, 'msg': '密码不能为空'}
                find_password.status = True
                find_password.save()
                return JsonResponse(msg)
            except Exception as ex:
                # 记日志 ex
                msg = {'code': 404, 'msg': "出错了请刷新页面"}
                return JsonResponse(msg)
        else:
            msg = {'code': 402, 'msg': "两次密码不一致"}
            return JsonResponse(msg)


# 个人中心
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        uid = request.user.id
        qc = QuestionsCollection.objects.filter(user_id=uid)
        ql = Questionsliker.objects.filter(user_id=uid)
        boc = []
        obl = []
        for i in qc:
            qc_id = i.question_id
            if i.status==True:
                questionc = Questions.objects.get(id=qc_id)
                boc.append(questionc)
        for i in ql:
            if i.status == True:
                ql_id = i.question_id
                questionl = Questions.objects.get(id=ql_id)
                obl.append(questionl)

        return render(request, "uc_base.html", {'obc': boc, 'obl': obl})

    def post(self, request):
        tp = request.POST.get('category')
        if tp == '1':
            try:
                if request.POST.get("email"):
                    request.user.email = request.POST.get("email")
                if request.POST.get("mobile"):
                    request.user.mobile = request.POST.get("mobile")
                print(request.POST.get('qq'))
                if request.POST.get("qq"):
                    request.user.qq = request.POST.get("qq")
                print(request.POST.get("name"))
                if request.POST.get("name"):
                    request.user.username = request.POST.get("name")
                request.user.save()
                ret_info = {'code': 200,
                            'username': request.user.username,
                            'qq': request.user.qq,
                            'email': request.user.email,
                            'mobile': request.user.mobile,
                            }
                return JsonResponse(ret_info)
            except Exception as ex:
                ret_info = {"code": 200, "msg": '失败了'}
                return JsonResponse(ret_info)
        elif tp == "2":
            old_password = request.POST.get("oldpassword")
            new_password1 = request.POST.get("newpassword1")
            new_password2 = request.POST.get("newpassword2")
            if len(old_password) == 0:
                ret_info = {"code": 400, "msg": "旧密码不能为空~"}
                return JsonResponse(ret_info)

            if len(new_password1) == 0 or len(new_password2) == 0:
                ret_info = {"code": 400, "msg": "新密码不能为空~"}
                return JsonResponse(ret_info)

            else:
                ## 前端验证 new_password1 == new_password2 才能提交
                if new_password1 != new_password2:
                    ret_info = {"code": 400, "msg": "两次新密码不一致~"}
                else:
                    if new_password1 == old_password:
                        ret_info = {"code": 400, "msg": "新密码和旧密码不能一样~"}
                    else:
                        user = auth.authenticate(username=request.user.username, password=old_password)
                        if user:
                            user.set_password(new_password1)
                            user.save()
                            auth.logout(request)
                            # auth.update_session_auth_hash(request, user)
                            ret_info = {"code": 200, "msg": "修改成功，请返回主页登录~"}
                        else:
                            ret_info = {"code": 400, "msg": "旧密码不正确~"}
                return JsonResponse(ret_info)

# 获取手机验证码
def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        # 获取ajax提取的数据
        mobile = request.GET.get("mobile")
        print(mobile)
        #
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        # global yanzhenma
        yanzhenma.append(mobile_captcha)
        print(mobile_captcha)
        print(yanzhenma)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)

# 获取图形验证码
def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type + base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)

# 检验
def check_captcha(request):
    ret = {"code": 400, "msg": "验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code', '')
    session_captcha_code = request.session.get('captcha_code', '')
    print(post_captcha_code, session_captcha_code)
    if post_captcha_code and post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
    return JsonResponse(ret)
