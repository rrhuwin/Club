from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from apps.count.models import News
from .models import Video
import page_splie
import json
import re
import time
from libs import search
from django.views.generic import View, DetailView



# 新闻首页
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
        return TemplateResponse(request, 'index.html', {'h': h_objec, "s": s_objec, 'q': q_objec, })


def my404(requset):
    return render(requset, '404.html')

# 获取音乐
def music(request):
    try:
        nname = request.POST.get("name")
        n =request.POST.get('num')
        ress = search.start(nname,str(n))

        for i in range(len(ress)):
            ress[i]['cover'] = 'http://p4.music.126.net/YXY1vPG5rtdV7w_cWDnNWw==/884007348732141.jpg?param=106x106'
        return HttpResponse(json.dumps(ress))
    except:
        ress={'artist_id':123}
        print(ress)
        return HttpResponse(json.dumps(ress))
#     换一批
def music2(request):
    try:
        n = request.POST.get("num")
        nname = request.POST.get("name")
        ress = search.start(nname,str(n))
        for i in range(len(ress)):
            ress[i]['cover'] = 'http://p4.music.126.net/YXY1vPG5rtdV7w_cWDnNWw==/884007348732141.jpg?param=106x106'
        return HttpResponse(json.dumps(ress))
    except:
        ress={'artist_id':123}
        return HttpResponse(json.dumps(ress))



# 新闻
def news(request, tp, page):
    if request.method == "GET":
        banner = News.objects.filter(category_id__in=[1, 2, 3]).order_by('-time')[0:11]

        if tp == 'h':
            cout = News.objects.filter(category_id=1).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/content/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=1).order_by('-news_id')[page_info.start():page_info.end()]
            return TemplateResponse(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info,"banner":banner})
        elif tp == 's':
            cout = News.objects.filter(category_id=2).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/content/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=2).order_by('-news_id')[page_info.start():page_info.end()]
            return TemplateResponse(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info,"banner":banner})
        elif tp == 'q':
            cout = News.objects.filter(category_id=3).count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/content/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id=3).order_by('-news_id')[page_info.start():page_info.end()]
            return TemplateResponse(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info,"banner":banner})
        elif tp == 'a':
            cout = News.objects.all().count()
            # c_obj = News.objects.filter(category_id=1).order_by('-news_id')[0:8]
            page_info = page_splie.Pageinfo(int(page), cout, 6, '/content/news/', tp, showpage=7)
            z_c_obj = News.objects.filter(category_id__lte=3).order_by('-time')[page_info.start():page_info.end()]
            return TemplateResponse(request, 'news.html', {'z_c_obj': z_c_obj, "pageinfo": page_info,"banner":banner})
        else:
            return TemplateResponse(request, 'news.html')

# 内容
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

# 古人
def ancient(request):
    if request.method == 'GET':

        cc = News.objects.filter(category_id=4)
        return TemplateResponse(request, 'ancient.html', {'cat': cc})
    else:
        return TemplateResponse(request, 'ancient.html')


def ancient_cont(request, p_id):
    if request.method == "GET":
        p_id = int(p_id)
        content = News.objects.get(news_id=p_id)
        return TemplateResponse(request, 'a_contact.html', {'content': content})

# 小技巧
def bsi(request):
    if request.method == 'GET':

        cc = News.objects.filter(category_id=5)
        return TemplateResponse(request, 'bsi.html', {'cat': cc})
    else:
        return TemplateResponse(request, 'bsi.html')


def bsi_cont(request, p_id):
    if request.method == "GET":
        p_id = int(p_id)
        content = News.objects.get(news_id=p_id)
        return TemplateResponse(request, 'bsi_contents.html', {'content': content})
