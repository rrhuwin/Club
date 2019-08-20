# coding=gbk
# 人生苦短，我用python
__auther__ = 'Mr.Hu'

import requests
import re
import os
import django
from bs4 import BeautifulSoup
import time
# i = input('请输出要查询的：')
# url =f'https://sffc.sh-service.com/wx_miniprogram/sites/feiguan/trashTypes_2/Handler/Handler.ashx?a=GET_KEYWORDS&kw={i}'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# a=requests.get(url=url,headers=header).text
# print(a)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recover.settings")
django.setup()

from apps.questions.models import Questions


# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# url= 'http://www.xzwonderful.com/newsCenter/articleDetails19.html'
# res=requests.get(url=url,headers=header)
# # print(res.text)
# soup = BeautifulSoup(res.text, 'lxml')
# s= soup.select('.artical-detail > p > span ')
# an= soup.select('.artical-detail > p > span span ')
# timu=[]
# answer=[]
# chose=['干垃圾','湿垃圾','可回收垃圾','有害垃圾','不进入垃圾系统']
# jiexi=[]
# j=0
# q=0
# x=0
# # 获取答案
# for i in an:
#     xx = re.findall(r'<span style="color: rgb\(255, 0, 0\);"><strong>(.*)</strong></span>|<span style="color: rgb\(255, 0, 0\);">(.*)</span>',str(i))
#     if len(xx)>=1:
#         j += 1
#         answer.append(str(xx[0][0]+xx[0][1]))
# # 获取题目
# timu01=[]
# for i in s :
#     j+=1
#     al = re.findall(r'<span style="font-family: 微软雅黑, ">([\u4e00-\u9fa5]{1,2}：.*)</span>',str(i))
#     if len(al)>=1:
#         timu01.append(al[0])
# for i in range(0,len(timu01),3):
#     q+=1
#     tm = re.findall(r'[\u4e00-\u9fa5]：(.*)', str(timu01[i]))
#     # print(tm)
#     timu.append(str(tm[0]))
#
# # 获取解析
# for i in range(2,len(timu01),3):
#     x+=1
#     jiexi.append(str(timu01[i]))

timu = [
    '导致水资源不足和用水紧张的原因是多方面的，下列说法中与此无关的是()',
    '为解决我国水资源供应紧张的矛盾，作为中学生的我们首先应做到的而且在日常生活中可以做到的是()',
    '下列措施中，不可能减轻水污染的是()',
    '我国主要的淡水资源是()',
    '我国水资源的空间分布特点是()',
    '解决水资源地区分布不均的有效办法之一是()',
    '我国水资源时间分布的特点是()',
    '修建水库的目的在于()',
    '我国最大的渔场是()',
    '我国最大的盐场是()',
    '南水北调工程东线方案的主要优势是()',
    '能缓解华北地区水源短缺的重大工程是()',
    '下列做法中不符合“因地制宜”利用土地资源的是()',
    '对于可再生资源的利用，下列说法正确的是()',
    '下列土地资源的利用不合理的是()',
    '随着人口的增长，总量越来越少，甚至有可能枯竭的自然资源是()',
    '构建节约型社会成为“十一五”规划的重要任务。下列做法与此相违背的是()',
    """
    关于我国地理事物叙述正确的是() 
    ①地势东高西低，呈阶梯状分布  ②气候复杂多样，季风气候显著  ③领土位于亚洲东部，太平洋西岸  ④自然资源总量丰富，人均占有量位居世界前列  ⑤是世界上人口最多的国家
    """,
    '我国第一大能源是()',
    '我国山区面积广大，其劣势是()',
    '我国正在建设中的“三峡水利枢纽工程”主要是为了解决学()',
    '富饶美丽的祖国海洋中，渔场和油气数量最多，也是产量最多的是()',

]
# 选项
xuax = [
    ['水资源时空分布不均', '水污染、水浪费严重', '人类对淡水的需求量增大', '兴修水利工程'],
    ['开采地下水', '人工降雨', '治理水污染', '节约用水'],
    ['减少农药、化肥的使用', '污水处理，达标排放', '农田采用大水漫灌的方式', '少使用洗涤剂和清洁剂'],
    ['江河湖泊水', '高山冰雪融水', '大气水', '地下水'],
    ['北方多，南方少', '西北多，西南少', '南方多，北方少', '东北多，西南少'],
    ['兴修水库', '节约用水', '跨流域调水', '开发地下水'],
    ['冬春多，夏秋少', '冬春少，夏秋多', '东部多，西部少', '东部少，西部多'],
    ['调节径流量的时间变化', '改变水资源的空间分布', '节约水资源', '发展淡水养殖业'],
    ['黄渤海渔场', '南海沿岸渔场', '舟山渔场', '北部湾渔场'],
    ['长芦盐场', '台湾西部盐场', '柴达木盐场', '莺歌海盐场'],
    ['输水线路较短', '人口少，最为经济', '可以利用已有河道及天然湖泊', '南高北低方便引水'],
    ['西电东输', '青藏铁路', '西所东输', '南水北调'],
    ['山区地形崎岖，适宜发展林业', '内蒙古草原地势平坦，适宜发展种植业', '沿海滩涂可发展养殖业', '平原地区地势平坦，土地肥沃，应发展耕作业'],
    ['可长时期地更新、再生，永续利用', '也要合理利用，注意保护和培育', '用一点就少一点，不能循环使用', '尽量少开发利用'],
    ['平原、盆地多发展耕地', '高原发展畜牧业', '山地可发展林业', '在耕地上修建高楼大厦'],
    ['水资源', '气候资源', '海洋资源', '煤炭资源'],
    ['完善再生资源回收利用体系', '努力发展循环经济，实行清洁生产', '大力发展传统工业和粗放农业', '应用现代科技改善生产条件，提高资源利用率'],
    ['①②④', '②③⑤', '①③⑤', '③④⑤'],
    ['煤炭', '石油', '水能', '核能'],
    ['森林资源不足', '耕地资源不足', '水能资源不足', '动植物资源不足'],
    ['水污染问题', '水资源时间分配不均的问题学科网', '水资源空间分布不均的问题', '水资源总量不足的问题'],
    ['渤海', '东海', '南海', '黄海'],
]
answer = ['兴修水利工程', '开采地下水', '农田采用大水漫灌的方式', '江河湖泊水', '南方多，北方少', '跨流域调水', '冬春少，夏秋多', '调节径流量的时间变化',
          '舟山渔场', '长芦盐场', '可以利用已有河道及天然湖泊', '南水北调','内蒙古草原地势平坦，适宜发展种植业','也要合理利用，注意保护和培育', '在耕地上修建高楼大厦',
            '煤炭资源','大力发展传统工业和粗放农业', '②③⑤', '煤炭','耕地资源不足','水资源时间分配不均的问题学科网', '南海',
          ]
for i in range(len(answer)):
    time.sleep(5)
    Questions.objects.create(category_id=2,title=timu[i],answer=answer[i]
                             ,choose_A=xuax[i][0],choose_B=xuax[i][1],choose_C=xuax[i][2],choose_D=xuax[i][3],
                             )
    print("写入成功")