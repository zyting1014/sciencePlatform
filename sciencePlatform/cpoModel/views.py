from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return render(request, 'index.html')


def comment(request):
    return render(request, 'comment.html')


def mainModel(request):
    return render(request, 'mainModel.html')


def mainModelResult(request):
    return render(request, 'mainModelResult.html')


def empty(request):
    return render(request, 'empty.html')


def ajaxGetModel(request):
    # return 训练集日期 训练集城市 测试集日期 测试集城市 模型名称 特征数量 正负样本比例 上传时间
    item1 = {'trainDate': '20191001-20191007', 'trainCity': 'Beijing', 'testDate': '20191110-20191110',
             'testCity': 'Beijing',
             'modelName': 'LR', 'featureNums': '17', 'posWeight': '15', 'createTime': '20200101'}
    item2 = {'trainDate': '20191001-20191007', 'trainCity': 'Beijing', 'testDate': '20191110-20191110',
             'testCity': 'Beijing',
             'modelName': 'LR', 'featureNums': '17', 'posWeight': '15', 'createTime': '20200101'}

    data = {'data': [item1, item2]}

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


def ajaxGetTrainTestAuc(request):
    import os
    BASE_DIR = '/home/tina/zhuyuting/毕设_20200108备份/毕设/实验数据'
    FILE_NAME = '17维原始特征20190701_20190707-20190710_cpo.txt'
    filePath = os.path.join(BASE_DIR, FILE_NAME)
    f = open(filePath)
    train_auc = []
    test_auc = []
    featureKey = []
    featureImportance = []
    for line in f:
        if line.find('train-auc') != -1:
            # auc
            pos1 = line.find('train-auc')
            pos2 = line.find('test-auc')
            auc1 = float(line[pos1 + 10:pos2].strip())
            auc2 = float(line[pos2 + 9:].strip())
            train_auc.append(auc1)
            test_auc.append(auc2)
        elif line.find('key') != -1:
            # key
            kName = line[line.find('key') + 4:line.find(',')]
            kValue = int(line[line.find('val') + 4:].strip())
            featureKey.append(kName)
            featureImportance.append(kValue)

    data = {'train_auc': train_auc, 'test_auc': test_auc,
            'featureKey': featureKey, 'featureImportance': featureImportance}

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')