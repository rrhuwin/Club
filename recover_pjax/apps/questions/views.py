from django.shortcuts import render, HttpResponse
from .models import Questions, QuestionsCollection, Questionsliker
from django.http import JsonResponse
import random
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
import json

#垃圾分类类，随机生成
def hdetails(request):
    uid = request.user.id
    L = [random.randint(0, 76) for _ in range(6)]
    obj1 = Questions.objects.filter(category_id=1)[L[0]]
    obj2 = Questions.objects.filter(category_id=1)[L[1]]
    obj3 = Questions.objects.filter(category_id=1)[L[2]]
    obj4 = Questions.objects.filter(category_id=1)[L[3]]
    obj5 = Questions.objects.filter(category_id=1)[L[4]]
    obj6 = Questions.objects.filter(category_id=1)[L[5]]
    if not uid:
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'h',
            'bor': 'bor_bottom',
            'status': 'False'
        }
        return render(request, 'questions.html', msg)
    if uid:
        q_id1 = obj1.id
        q_id2 = obj2.id
        q_id3 = obj3.id
        q_id4 = obj4.id
        q_id5 = obj5.id
        q_id6 = obj6.id

        userinfo = QuestionsCollection.objects.filter(user_id=uid)
        questinfo1 = userinfo.filter(question_id=q_id1)
        questinfo2 = userinfo.filter(question_id=q_id2)
        questinfo3 = userinfo.filter(question_id=q_id3)
        questinfo4 = userinfo.filter(question_id=q_id4)
        questinfo5 = userinfo.filter(question_id=q_id5)
        questinfo6 = userinfo.filter(question_id=q_id6)
        userinfo1 = Questionsliker.objects.filter(user_id=uid)
        questinfo11 = userinfo1.filter(question_id=q_id1)
        questinfo12 = userinfo1.filter(question_id=q_id2)
        questinfo13 = userinfo1.filter(question_id=q_id3)
        questinfo14 = userinfo1.filter(question_id=q_id4)
        questinfo15 = userinfo1.filter(question_id=q_id5)
        questinfo16 = userinfo1.filter(question_id=q_id6)
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'h',
            'bor': 'bor_bottom',
            'status1': 'False',
            'status2': 'False',
            'status3': 'False',
            'status4': 'False',
            'status5': 'False',
            'status6': 'False',
            'status11': 'False',
            'status12': 'False',
            'status13': 'False',
            'status14': 'False',
            'status15': 'False',
            'status16': 'False',
        }
        if questinfo1:
            if questinfo1[0].status:
                msg['status1'] = 'True'
        if questinfo2:
            if questinfo2[0].status:
                msg['status2'] = 'True'
        if questinfo3:
            if questinfo3[0].status:
                msg['status3'] = 'True'
        if questinfo4:
            if questinfo4[0].status:
                msg['status4'] = 'True'
        if questinfo5:
            if questinfo5[0].status:
                msg['status5'] = 'True'
        if questinfo6:
            if questinfo6[0].status:
                msg['status6'] = 'True'
        if questinfo11:
            if questinfo11[0].status:
                msg['status11'] = 'True'
        if questinfo12:
            if questinfo12[0].status:
                msg['status12'] = 'True'
        if questinfo13:
            if questinfo13[0].status:
                msg['status13'] = 'True'
        if questinfo14:
            if questinfo14[0].status:
                msg['status14'] = 'True'
        if questinfo15:
            if questinfo15[0].status:
                msg['status15'] = 'True'
        if questinfo16:
            if questinfo16[0].status:
                msg['status16'] = 'True'
        return render(request, 'questions.html', msg)

#水资源类，随机生成
def sdetails(request):
    uid = request.user.id

    L = [random.randint(0, 21) for _ in range(6)]
    print(L)
    obj1 = Questions.objects.filter(category_id=2)[L[0]]
    obj2 = Questions.objects.filter(category_id=2)[L[1]]
    obj3 = Questions.objects.filter(category_id=2)[L[2]]
    obj4 = Questions.objects.filter(category_id=2)[L[3]]
    obj5 = Questions.objects.filter(category_id=2)[L[4]]
    obj6 = Questions.objects.filter(category_id=2)[L[5]]

    if not uid:
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 's',
            'bor': 'bor_bottom',
            'status': 'False'
        }
        return render(request, 'questions.html', msg)
    if uid:
        q_id1 = obj1.id
        q_id2 = obj2.id
        q_id3 = obj3.id
        q_id4 = obj4.id
        q_id5 = obj5.id
        q_id6 = obj6.id
        userinfo = QuestionsCollection.objects.filter(user_id=uid)
        questinfo1 = userinfo.filter(question_id=q_id1)
        questinfo2 = userinfo.filter(question_id=q_id2)
        questinfo3 = userinfo.filter(question_id=q_id3)
        questinfo4 = userinfo.filter(question_id=q_id4)
        questinfo5 = userinfo.filter(question_id=q_id5)
        questinfo6 = userinfo.filter(question_id=q_id6)
        userinfo1 = Questionsliker.objects.filter(user_id=uid)
        questinfo11 = userinfo1.filter(question_id=q_id1)
        questinfo12 = userinfo1.filter(question_id=q_id2)
        questinfo13 = userinfo1.filter(question_id=q_id3)
        questinfo14 = userinfo1.filter(question_id=q_id4)
        questinfo15 = userinfo1.filter(question_id=q_id5)
        questinfo16 = userinfo1.filter(question_id=q_id6)
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 's',
            'bor': 'bor_bottom',
            'status1': 'False',
            'status2': 'False',
            'status3': 'False',
            'status4': 'False',
            'status5': 'False',
            'status6': 'False',
            'status11': 'False',
            'status12': 'False',
            'status13': 'False',
            'status14': 'False',
            'status15': 'False',
            'status16': 'False',
        }
        if questinfo1:
            if questinfo1[0].status:
                msg['status1'] = 'True'
        if questinfo2:
            if questinfo2[0].status:
                msg['status2'] = 'True'
        if questinfo3:
            if questinfo3[0].status:
                msg['status3'] = 'True'
        if questinfo4:
            if questinfo4[0].status:
                msg['status4'] = 'True'
        if questinfo5:
            if questinfo5[0].status:
                msg['status5'] = 'True'
        if questinfo6:
            if questinfo6[0].status:
                msg['status6'] = 'True'
        if questinfo11:
            if questinfo11[0].status:
                msg['status11'] = 'True'
        if questinfo12:
            if questinfo12[0].status:
                msg['status12'] = 'True'
        if questinfo13:
            if questinfo13[0].status:
                msg['status13'] = 'True'
        if questinfo14:
            if questinfo14[0].status:
                msg['status14'] = 'True'
        if questinfo15:
            if questinfo15[0].status:
                msg['status15'] = 'True'
        if questinfo16:
            if questinfo16[0].status:
                msg['status16'] = 'True'
        return render(request, 'questions.html', msg)

#总类，随机生成
def adetails(request):
    uid = request.user.id

    L = [random.randint(0, 97) for _ in range(6)]
    print(L)
    obj1 = Questions.objects.all()[L[0]]
    obj2 = Questions.objects.all()[L[1]]
    obj3 = Questions.objects.all()[L[2]]
    obj4 = Questions.objects.all()[L[3]]
    obj5 = Questions.objects.all()[L[4]]
    obj6 = Questions.objects.all()[L[5]]
    if not uid:
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'a',
            'bor': 'bor_bottom',
            'status': 'False'
        }
        return render(request, 'questions.html', msg)
    if uid:

        q_id1 = obj1.id
        q_id2 = obj2.id
        q_id3 = obj3.id
        q_id4 = obj4.id
        q_id5 = obj5.id
        q_id6 = obj6.id

        userinfo = QuestionsCollection.objects.filter(user_id=uid)
        questinfo1 = userinfo.filter(question_id=q_id1)
        questinfo2 = userinfo.filter(question_id=q_id2)
        questinfo3 = userinfo.filter(question_id=q_id3)
        questinfo4 = userinfo.filter(question_id=q_id4)
        questinfo5 = userinfo.filter(question_id=q_id5)
        questinfo6 = userinfo.filter(question_id=q_id6)
        userinfo1 = Questionsliker.objects.filter(user_id=uid)
        questinfo11 = userinfo1.filter(question_id=q_id1)
        questinfo12 = userinfo1.filter(question_id=q_id2)
        questinfo13 = userinfo1.filter(question_id=q_id3)
        questinfo14 = userinfo1.filter(question_id=q_id4)
        questinfo15 = userinfo1.filter(question_id=q_id5)
        questinfo16 = userinfo1.filter(question_id=q_id6)
        msg = {
            'obj1': obj1,
            'obj2': obj2,
            'obj3': obj3,
            'obj4': obj4,
            'obj5': obj5,
            'obj6': obj6,
            'cate': 'a',
            'bor': 'bor_bottom',
            'status1': 'False',
            'status2': 'False',
            'status3': 'False',
            'status4': 'False',
            'status5': 'False',
            'status6': 'False',
            'status11': 'False',
            'status12': 'False',
            'status13': 'False',
            'status14': 'False',
            'status15': 'False',
            'status16': 'False',
        }
        if questinfo1:
            if questinfo1[0].status:
                msg['status1'] = 'True'
        if questinfo2:
            if questinfo2[0].status:
                msg['status2'] = 'True'
        if questinfo3:
            if questinfo3[0].status:
                msg['status3'] = 'True'
        if questinfo4:
            if questinfo4[0].status:
                msg['status4'] = 'True'
        if questinfo5:
            if questinfo5[0].status:
                msg['status5'] = 'True'
        if questinfo6:
            if questinfo6[0].status:
                msg['status6'] = 'True'
        if questinfo11:
            if questinfo11[0].status:
                msg['status11'] = 'True'
        if questinfo12:
            if questinfo12[0].status:
                msg['status12'] = 'True'
        if questinfo13:
            if questinfo13[0].status:
                msg['status13'] = 'True'
        if questinfo14:
            if questinfo14[0].status:
                msg['status14'] = 'True'
        if questinfo15:
            if questinfo15[0].status:
                msg['status15'] = 'True'
        if questinfo16:
            if questinfo16[0].status:
                msg['status16'] = 'True'
        return render(request, 'questions.html', msg)

# 验证答案
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

# 取消收藏
def cancelc(request):
    cid = request.POST.get('cid')
    obj = QuestionsCollection.objects.get(question_id=cid)
    obj.status = 0
    obj.save()
    msg = {'code': 200}
    return HttpResponse(json.dumps(msg))

#取消点赞
def canceld(request):
    uid = request.user.id
    did = request.POST.get('did')
    obj = Questionsliker.objects.get_or_create(user_id=uid, question_id=did)
    obj[0].status = False
    obj[0].save()
    msg = {'code': 200}
    return HttpResponse(json.dumps(msg))

# 收藏
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

#点赞
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
        print(msg)
        ret_info = {"code": 200, "msg": msg}
        return JsonResponse(ret_info)
