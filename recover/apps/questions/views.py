from django.shortcuts import render
from .models import Questions, QuestionsCollection, Questionsliker
from django.http import JsonResponse
import random
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView


# Create your views here.

def details(request):
    if request.is_ajax():
        L = [random.randint(0, 77) for _ in range(6)]
        print(L)
        obj1 = Questions.objects.all()[L[0]]
        obj2 = Questions.objects.all()[L[1]]
        obj3 = Questions.objects.all()[L[2]]
        obj4 = Questions.objects.all()[L[3]]
        obj5 = Questions.objects.all()[L[4]]
        obj6 = Questions.objects.all()[L[5]]
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'a'
        }
        return JsonResponse(msg)
    else:
        L = [random.randint(0, 77) for _ in range(6)]
        print(L)
        obj1 = Questions.objects.all()[L[0]]
        obj2 = Questions.objects.all()[L[1]]
        obj3 = Questions.objects.all()[L[2]]
        obj4 = Questions.objects.all()[L[3]]
        obj5 = Questions.objects.all()[L[4]]
        obj6 = Questions.objects.all()[L[5]]
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'a'

        }
        return render(request, 'questions.html', msg)


def hdetails(request):
    L = [random.randint(0, 76) for _ in range(6)]
    print(L)
    obj1 = Questions.objects.filter(category_id=1)[L[0]]
    obj2 = Questions.objects.filter(category_id=1)[L[1]]
    obj3 = Questions.objects.filter(category_id=1)[L[2]]
    obj4 = Questions.objects.filter(category_id=1)[L[3]]
    obj5 = Questions.objects.filter(category_id=1)[L[4]]
    obj6 = Questions.objects.filter(category_id=1)[L[5]]
    msg = {
        'obj1': obj1,
        'obj2': obj2,
        'obj3': obj3,
        'obj4': obj4,
        'obj5': obj5,
        'obj6': obj6,
        'cate': 'h'

    }

    # for i in ids[0]:
    #     print(i)
    return render(request, 'questions.html', msg)


def sdetails(request):
    L = [random.randint(0, 21) for _ in range(6)]
    print(L)
    obj1 = Questions.objects.filter(category_id=2)[L[0]]
    obj2 = Questions.objects.filter(category_id=2)[L[1]]
    obj3 = Questions.objects.filter(category_id=2)[L[2]]
    obj4 = Questions.objects.filter(category_id=2)[L[3]]
    obj5 = Questions.objects.filter(category_id=2)[L[4]]
    obj6 = Questions.objects.filter(category_id=2)[L[5]]
    msg = {
        'obj1': obj1,
        'obj2': obj2,
        'obj3': obj3,
        'obj4': obj4,
        'obj5': obj5,
        'obj6': obj6,
        'cate': 's'

    }

    # for i in ids[0]:
    #     print(i)
    return render(request, 'questions.html', msg)


def check(request):
    # answer = {'干垃圾': 1, '湿垃圾': 2, '可回收垃圾': 3, '有害垃圾': 4, '不进入垃圾系统': 5}

    answers = request.POST.get('answer')
    ids = request.POST.get('ids')
    print(ids)
    obj = Questions.objects.get(id=ids)
    if obj.answer == answers:
        msg = {'status': 'success', 'msg': 'yes', 'answer': obj.answer, 'you': answers}
        print('dui')
        return JsonResponse(msg)

    else:
        msg = {'status': 'success', 'msg': 'no', 'answer': obj.answer, 'you': answers}
        print('cuo')
        return JsonResponse(msg)


class QuestionCollectionView(LoginRequiredMixin, View):
    def get(self, request, id):
        """
        当用户点击该题目时，首先获取该题目，并检查该题目是否已被操作过
        修改当前题目的收藏状态
        返回json数据
        id => 题目的ID
        """
        question = Questions.objects.get(id=id)
        result = QuestionsCollection.objects.get_or_create(user=request.user, question=question)
        # result是一个元组，第一参数是instance, 第二个参数是true和false
        # True表示新创建,False表示老数据
        question_collection = result[0]
        if not result[1]:
            # print('x',answer_collection.status)
            if question_collection.status:
                question_collection.status = False
            else:
                question_collection.status = True
        question_collection.save()
        msg = model_to_dict(question_collection)
        ret_info = {"code": 200, "msg": msg}
        return JsonResponse(ret_info)


class QuestionlikeView(LoginRequiredMixin, View):
    def get(self, request, id):
        """
        当用户点击该题目时，首先获取该题目，并检查该题目是否已被操作过
        修改当前题目的收藏状态
        返回json数据
        id => 题目的ID
        """
        question = Questions.objects.get(id=id)
        result = Questionsliker.objects.get_or_create(user=request.user, question=question)
        # result是一个元组，第一参数是instance, 第二个参数是true和false
        # True表示新创建,False表示老数据
        question_like_collection = result[0]
        if not result[1]:
            # print('x',answer_collection.status)
            if question_like_collection.status:
                question_like_collection.status = False
            else:
                question_like_collection.status = True
        question_like_collection.save()
        msg = model_to_dict(question_like_collection)
        ret_info = {"code": 200, "msg": msg}
        return JsonResponse(ret_info)
