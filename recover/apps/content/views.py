from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.count.models import News
from .models import Video
from libs import page_splie
import json
import re
from libs import  search
from django.views.generic import View, DetailView


# Create your views here.
# @login_required()
# def about(request):
#     user = request.session.get('user')
#     print(user)
#     return render(request, 'about.html', {'user': user})


def index(request):
    if request.session.get('user'):
        h_objec = News.objects.filter(category_id=1).order_by('-news_id')[0]
        s_objec = News.objects.filter(category_id=2).order_by('-news_id')[0]
        q_objec = News.objects.filter(category_id=3).order_by('-news_id')[0]
        user = request.session.get('user', 'me')
        return render(request, 'index.html', {'h': h_objec, "s": s_objec, 'q': q_objec, 'user': user})
    else:
        h_objec = News.objects.filter(category_id=1).order_by('-news_id')[0]
        s_objec = News.objects.filter(category_id=2).order_by('-news_id')[0]
        q_objec = News.objects.filter(category_id=3).order_by('-news_id')[0]
        return render(request, 'index.html', {'h': h_objec, "s": s_objec, 'q': q_objec, })


def my404(requset):
    return render(requset, '404.html')


def music(request):
    ress = [{'artist_id': '5781', 'artist': '薛之谦', 'mp3': 'http://music.163.com/song/media/outer/url?id=27955653.mp3',
             'title': '你还要我怎样'}, {'artist_id': '12444454', 'artist': '董嘉鸿',
                                  'mp3': 'http://music.163.com/song/media/outer/url?id=1309073929.mp3', 'title': '慢自由'},
            {'artist_id': '8330/5346', 'artist': '卢巧音/王力宏',
             'mp3': 'http://music.163.com/song/media/outer/url?id=27713963.mp3', 'title': '好心分手'},
            {'artist_id': '12347360', 'artist': 'JC陈泳彤',
             'mp3': 'http://music.163.com/song/media/outer/url?id=468513829.mp3', 'title': '说散就散'},
            {'artist_id': '6462', 'artist': '张敬轩', 'mp3': 'http://music.163.com/song/media/outer/url?id=189323.mp3',
             'title': '断点'},
            {'artist_id': '2112', 'artist': '陈小春', 'mp3': 'http://music.163.com/song/media/outer/url?id=63650.mp3',
             'title': '独家记忆'},
            {'artist_id': '7409', 'artist': '岑宁儿', 'mp3': 'http://music.163.com/song/media/outer/url?id=483671599.mp3',
             'title': '追光者'}, {'artist_id': '12085562', 'artist': '买辣椒也用券',
                               'mp3': 'http://music.163.com/song/media/outer/url?id=1330348068.mp3', 'title': '起风了'},
            {'artist_id': '8334', 'artist': '刘惜君', 'mp3': 'http://music.163.com/song/media/outer/url?id=255294.mp3',
             'title': '我很快乐'},
            {'artist_id': '10558', 'artist': '周笔畅', 'mp3': 'http://music.163.com/song/media/outer/url?id=531295576.mp3',
             'title': '最美的期待'},
            {'artist_id': '9548', 'artist': '田馥甄', 'mp3': 'http://music.163.com/song/media/outer/url?id=28018075.mp3',
             'title': '你就不要想起我'}, {'artist_id': '28083340', 'artist': '王北车',
                                   'mp3': 'http://music.163.com/song/media/outer/url?id=1294899063.mp3', 'title': '陷阱'},
            {'artist_id': '13906123', 'artist': '张紫豪',
             'mp3': 'http://music.163.com/song/media/outer/url?id=553755659.mp3', 'title': '可不可以'},
            {'artist_id': '5771', 'artist': '许嵩', 'mp3': 'http://music.163.com/song/media/outer/url?id=167876.mp3',
             'title': '有何不可'},
            {'artist_id': '1053026', 'artist': '曾惜', 'mp3': 'http://music.163.com/song/media/outer/url?id=30987293.mp3',
             'title': '讲真的'}, {'artist_id': '1038040', 'artist': '赵紫骅',
                               'mp3': 'http://music.163.com/song/media/outer/url?id=29759733.mp3', 'title': '可乐'},
            {'artist_id': '9255', 'artist': '任然', 'mp3': 'http://music.163.com/song/media/outer/url?id=526464293.mp3',
             'title': '空空如也 '}, {'artist_id': '4678/3459', 'artist': '南宫嘉骏/姜玉阳',
                                 'mp3': 'http://music.163.com/song/media/outer/url?id=33887645.mp3', 'title': '回忆总想哭'},
            {'artist_id': '12174521', 'artist': '音阙诗听',
             'mp3': 'http://music.163.com/song/media/outer/url?id=452986458.mp3', 'title': '红昭愿'},
            {'artist_id': '12302029', 'artist': '王冕',
             'mp3': 'http://music.163.com/song/media/outer/url?id=461519272.mp3', 'title': '勉为其难'},
            {'artist_id': '12262303', 'artist': '于果',
             'mp3': 'http://music.163.com/song/media/outer/url?id=534542079.mp3', 'title': '侧脸'},
            {'artist_id': '3685', 'artist': '林宥嘉', 'mp3': 'http://music.163.com/song/media/outer/url?id=108390.mp3',
             'title': '说谎'},
            {'artist_id': '12707', 'artist': '苏打绿', 'mp3': 'http://music.163.com/song/media/outer/url?id=26524510.mp3',
             'title': '我好想你'},
            {'artist_id': '4292', 'artist': '李荣浩', 'mp3': 'http://music.163.com/song/media/outer/url?id=1293886117.mp3',
             'title': '年少有为'},
            {'artist_id': '840134', 'artist': '刘瑞琦', 'mp3': 'http://music.163.com/song/media/outer/url?id=27867140.mp3',
             'title': '房间'}, {'artist_id': '12292708', 'artist': '周思涵',
                              'mp3': 'http://music.163.com/song/media/outer/url?id=445665094.mp3', 'title': '过客'},
            {'artist_id': '1044203', 'artist': '郭旭', 'mp3': 'http://music.163.com/song/media/outer/url?id=29850531.mp3',
             'title': '不找了'},
            {'artist_id': '893259', 'artist': '金玟岐', 'mp3': 'http://music.163.com/song/media/outer/url?id=28285910.mp3',
             'title': '岁月神偷'}, {'artist_id': '12760978', 'artist': '广东雨神',
                                'mp3': 'http://music.163.com/song/media/outer/url?id=513791211.mp3',
                                'title': '广东十年爱情故事'}]

    for i in range(len(ress)):
        ress[i]['cover'] = 'http://p4.music.126.net/YXY1vPG5rtdV7w_cWDnNWw==/884007348732141.jpg?param=106x106'
    return render(request, 'music.html', {'id': ress})


class Show(View):
    def get(self, request):
        video = Video.objects.all()
        l=[1,2,3,4,5,6,7,8]
        return render(request, 'video.html', {'vide': video,'li':l})
    # def post(self):
    # def post(self, request):
    #     email = request.POST.get("email")
    #     if email and User.objects.filter(email=email):
    #         verify_code = "".join(random.choices(string.ascii_lowercase + string.digits, k=128))
    #         url = f"{request.scheme}://{request.META['HTTP_HOST']}/count/newpass/{verify_code}?email={email}"
    #         ret = FindPassword.objects.get_or_create(email=email)
    #         # (<FindPassword: FindPassword object>, True)
    #         ret[0].verify_code = verify_code
    #         ret[0].status = False
    #         ret[0].save()
    #
    #         send_mail('注册用户验证信息', url, None, [email])
    #         msg = {'code': 200, 'msg': "邮件发送成功，请登录邮箱查看！"}
    #         return JsonResponse(msg)
    #     else:
    #         msg = {'code': 404, 'msg': "输入的邮箱不存在！"}
    #         return JsonResponse(msg)


def news(request, tp, page):
    if request.method == "GET":
        if tp == 'h':
            cout = News.objects.filter(category_id=1).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=1).order_by('-news_id')[page_info.start():page_info.end()]
            return render(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info})
        elif tp == 's':
            cout = News.objects.filter(category_id=2).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=2).order_by('-news_id')[page_info.start():page_info.end()]
            return render(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info})
        elif tp == 'q':
            cout = News.objects.filter(category_id=3).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=3).order_by('-news_id')[page_info.start():page_info.end()]
            return render(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info})
        elif tp == 'a':
            cout = News.objects.all().count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id__lte=3).order_by('-time')[page_info.start():page_info.end()]
            return render(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info})
        else:
            return render(request, 'news.html')


def contents(request, tpa, pn):
    if request.method == "GET":
        if tpa == "h":
            content = News.objects.get(news_id=int(pn))
            return render(request, 'contents.html', {'cont': content})
        elif tpa == "s":
            content = News.objects.get(news_id=int(pn))
            return render(request, 'contents.html', {'cont': content})
        elif tpa == "q":
            content = News.objects.get(news_id=int(pn))
            return render(request, 'contents.html', {'cont': content})
        else:
            return render(request, 'news.html')


def ancient(request):
    if request.method == 'GET':

        cc = News.objects.filter(category_id=4)
        return render(request, 'ancient.html', {'cat': cc})
    else:
        return render(request, 'ancient.html')


def ancient_cont(request, p_id):
    if request.method == "GET":
        p_id = int(p_id)
        content = News.objects.get(news_id=p_id)
        return render(request, 'a_contact.html', {'content': content})


def bsi(request):
    if request.method == 'GET':

        cc = News.objects.filter(category_id=5)
        return render(request, 'bsi.html', {'cat': cc})
    else:
        return render(request, 'bsi.html')


def bsi_cont(request, p_id):
    if request.method == "GET":
        p_id = int(p_id)
        content = News.objects.get(news_id=p_id)
        return render(request, 'bsi_contents.html', {'content': content})
