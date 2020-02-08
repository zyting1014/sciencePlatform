from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
    return render(request,'index.html')

def comment(request):
    return render(request,'comment.html')

def mainModel(request):
    return render(request,'mainModel.html')

def empty(request):
    return render(request,'empty.html')



def ajaxGetModel(request):
    # return 训练集日期 训练集城市 测试集日期 测试集城市 模型名称 特征数量 正负样本比例 上传时间
    item1 = {'trainDate': '20191001-20191007', 'trainCity': 'Beijing', 'testDate': '20191110-20191110', 'testCity': 'Beijing',
             'modelName': 'LR', 'featureNums': '17', 'posWeight': '15', 'createTime': '20200101'}
    item2 = {'trainDate': '20191001-20191007', 'trainCity': 'Beijing', 'testDate': '20191110-20191110', 'testCity': 'Beijing',
             'modelName': 'LR', 'featureNums': '17', 'posWeight': '15', 'createTime': '20200101'}

    data = {'data': [item1, item2]}

    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json')
    # return render(request,'empty.html')