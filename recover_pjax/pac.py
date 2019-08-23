# !/user/bin/python
# -*- coding:utf-8 -*-
__auther__ = 'whtie'
import requests
from bs4 import BeautifulSoup
import json
import re
import os
import django
import time

# 新闻内容

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recover.settings")
django.setup()

from apps.count.models import News


def spsder(url, ip, tp):
    abstract = []
    title = []
    content = []
    # 新闻主页
    time_list = []
    small_abstract = []
    a_img = []
    a_titles = []
    ids = []
    for i in range(1, 2):
        a_l = []
        header = {
            'Host': 'www.hbzhan.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN, zh;q=0.9',
            'Host': 'www.hbzhan.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit /537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        time.sleep(20)
        res = requests.get(url=url, headers=header)
        soup = BeautifulSoup(res.text, 'lxml')
        h3_a = soup.select('.leftBox > h3 > a')
        a = soup.select('.leftBox > a')
        p = soup.select('.leftBox > p')
        abt = soup.select('.time')
        # time列表
        for t in abt:
            ti = re.findall(r'<span class="time">(.*)</span>', str(t))
            time_list.append(str(ti[0]))
        print('time生成成功')
        # p的列表
        for y in p:
            p_n = re.findall(r'(.*)<a', str(y))
            p_last = p_n[0] + "</p>"
            small_abstract.append(str(p_last))
        print('small_abstract生成成功')
        # a标签列表
        for x in a:
            a_img.append(str(x))
        print('a_img生成成功')
        # 拼接成h3标签列表
        for j in h3_a:
            h3_min = "<h3>" + str(j) + "</h3>"
            a_titles.append(h3_min)
        print('a_titles生成成功')
        # 、获取id
        for i in a:
            a_l.append(i['href'])
        # 每个新闻的连接
        print('id生成成功')
        # print(a_l)
        a_l2 = list(set(a_l))
        a_l2.sort(key=a_l.index)
        # 获取id
        for z in a_l2:
            res = re.findall(r'(\d{6})\.html$', z)
            ids.append(res[0])

        for x in range(15):
            print(f'{x}开始休息....')
            time.sleep(80)
            print('休息结束')
            res2 = requests.get(url=a_l2[x], headers=headers)
            time.sleep(5)
            soup1 = BeautifulSoup(res2.text, 'lxml')
            time.sleep(5)
            titles = soup1.select('.leftTop h2')
            time.sleep(5)
            abst = soup1.select('.abstract')
            time.sleep(5)
            contents = soup1.select('.newsContent')
            time.sleep(5)
            content.append(str(contents[0]))
            print('content生成成功')
            abstract.append(str(abst[0]))
            print('abstract生成成功')
            title.append(str(titles[0]))
            print('title生成成功')
            print('*' * 50)

    for i in range(15):
        n_title = re.sub(r'http:(.*)k"', f'/content/contents/{tp}/{ids[i]}" data-pjax="true"', a_titles[i])
        n_img = re.sub(r'http:(.*)k"', f'/content/contents/{tp}/{ids[i]}" data-pjax="true"', a_img[i])
        try:
            print(f'开始写数据{ids[i]}')
            time.sleep(10)
            idd = News.objects.get(news_id=ids[i])
            print('数据已存在！已跳过')
        except Exception:
            News.objects.create(
                news_id=ids[i], s_title=n_title,
                s_ab=small_abstract[i], img_url=n_img, time=time_list[i], title=title[i]
                , abstrat=abstract[i], content=content[i], category_id=ip)
            print(f'写入{ids[i]}成功')


url = ['http://www.hbzhan.com/news/t0/list_p2_k%e5%9e%83%e5%9c%be%e5%88%86%e7%b1%bb.html',
       'http://www.hbzhan.com/news/t0/list_p2_k%e6%b8%85%e6%b4%81%e8%83%bd%e6%ba%90.html',
       'http://www.hbzhan.com/news/t7418/list_p2.html',
       'http://www.hbzhan.com/news/t0/list_p1_k%e5%9e%83%e5%9c%be%e5%88%86%e7%b1%bb.html',
       'http://www.hbzhan.com/news/t0/list_p1_k%e6%b8%85%e6%b4%81%e8%83%bd%e6%ba%90.html',
       'http://www.hbzhan.com/news/t7418/list_p1.html',
       'http://www.hbzhan.com/news/t0/list_p3_k%e5%9e%83%e5%9c%be%e5%88%86%e7%b1%bb.html',
       'http://www.hbzhan.com/news/t0/list_p3_k%e6%b8%85%e6%b4%81%e8%83%bd%e6%ba%90.html',
       'http://www.hbzhan.com/news/t7418/list_p3.html',
       ]
u = [1, 3, 2,1, 3, 2,1, 3, 2]
tp = ['h', 'q', 's','h', 'q', 's','h', 'q', 's']
for i in range(0,8):
    time.sleep(30)
    spsder(url[i], u[i], tp[i])
    time.sleep(30)
