# coding=gbk
# 人生苦短，我用python
__auther__ = 'Mr.Hu'
import requests
from bs4 import BeautifulSoup
import json
import os
import django
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recover.settings")
django.setup()

from apps.content.models import Video


def func_first():
    header = {
        'Referer': 'https://search.bilibili.com/all?keyword=%E6%88%91%E6%83%B3%E5%90%83%E6%8E%89%E4%BD%A0%E7%9A%84%E8%83%B0%E8%84%8F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://api.bilibili.com/x/web-interface/search/all?highlight=1&keyword=%E7%8E%AF%E4%BF%9D&jsonp=jsonp'
    param = {
        'highlight': '1',
        'keyword': '你好',
        'jsonp': 'jsonp',

    }
    res = requests.get(url=url, headers=header).text
    res1 = json.loads(res)
    video = res1.get('data').get('result').get('video')
    #     标题
    title = []
    # 视频id
    vid = []
    # 图片地址
    img_url = []
    list = [0, 1, 3, 4, 6, 7, 8, 9, 14, 19]
    for i in list:
        img_url.append(video[i].get('pic'))
        vid.append(video[i].get('id'))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://search.bilibili.com/all?keyword=%E7%8E%AF%E4%BF%9D&order=totalrank&duration=0&tids_1=0'
    res5 = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(res5, 'lxml')
    titles = soup.select('.video > a')
    for i in list:
        title.append(titles[i]['title'])

    for j in range(len(vid)):
        time.sleep(3)
        Video.objects.create(titles=title[j], videoid=vid[j], imgurl=img_url[j])

func_first()

def pages_then_two():
    header = {
        'Referer': 'https://search.bilibili.com/all?keyword=%E6%88%91%E6%83%B3%E5%90%83%E6%8E%89%E4%BD%A0%E7%9A%84%E8%83%B0%E8%84%8F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E7%8E%AF%E4%BF%9D%E7%9F%AD%E7%89%87&page=2&jsonp=jsonp'
    res = requests.get(url=url, headers=header).text
    res1 = json.loads(res)
    video = res1.get('data').get('result')
    #     标题
    title = []
    # 视频id
    vid = []
    # 图片地址
    img_url = []
    for i in video:
        img_url.append(i.get('pic'))
        vid.append(i.get('id'))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://search.bilibili.com/all?keyword=%E7%8E%AF%E4%BF%9D%E7%9F%AD%E7%89%87&page=2'
    res5 = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(res5, 'lxml')
    titles = soup.select('.video > a')
    for i in titles:
        title.append(i['title'])

    for j in range(len(vid)):
        time.sleep(3)
        Video.objects.create(titles=title[j], videoid=vid[j], imgurl=img_url[j])


def pages_then_three():
    header = {
        'Referer': 'https://search.bilibili.com/all?keyword=%E6%88%91%E6%83%B3%E5%90%83%E6%8E%89%E4%BD%A0%E7%9A%84%E8%83%B0%E8%84%8F',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E7%8E%AF%E4%BF%9D%E7%9F%AD%E7%89%87&page=3&jsonp=jsonp'
    res = requests.get(url=url, headers=header).text
    res1 = json.loads(res)
    video = res1.get('data').get('result')
    #     标题
    title = []
    # 视频id
    vid = []
    # 图片地址
    img_url = []
    for i in video:
        img_url.append(i.get('pic'))
        vid.append(i.get('id'))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url = 'https://search.bilibili.com/all?keyword=%E7%8E%AF%E4%BF%9D%E7%9F%AD%E7%89%87&page=3'
    res5 = requests.get(url=url, headers=header).text
    soup = BeautifulSoup(res5, 'lxml')
    titles = soup.select('.video > a')
    for i in titles:
        title.append(i['title'])

    for j in range(len(vid)):
        time.sleep(3)
        Video.objects.create(titles=title[j], videoid=vid[j], imgurl=img_url[j])



func_first()
time.sleep(10)
pages_then_two()
time.sleep(10)


pages_then_three()