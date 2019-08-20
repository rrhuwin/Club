from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import requests
import json


def search(request):
    try:
        i = request.GET.get('kw')
        url = f'https://sffc.sh-service.com/wx_miniprogram/sites/feiguan/trashTypes_2/Handler/Handler.ashx?a=GET_KEYWORDS&kw={i}'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        a = requests.get(url=url, headers=header).text
        a1 = json.loads(a)
        kw = a1.get('kw_list')  # list
        k = {}
        # print(type(a1), a1)
        for j in a1.get('kw_arr'):
            n = j.get('Name')
            t = j.get('TypeKey')
            k[n] = t
        msg = {
            'kw': kw,
            'detail': k,
        }
        print(k)
        return JsonResponse(msg)
    except:
        print(1)
        msg = {
            'ak': 1,
        }
        return JsonResponse(msg)
