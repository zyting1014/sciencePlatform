from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return render(request, 'index.html')


def comment(request):
    return render(request, 'comment.html')


def dropRoute(request):
    return render(request, 'dropRoute.html')


def mainModel(request):
    return render(request, 'mainModel.html')


def mainModelResult(request):
    return render(request, 'mainModelResult.html')


def dValueEvaluation(request):
    return render(request, 'dValueEvaluation.html')


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
    trainTag = True
    allSampleTrain = 0;posSampleTrain = 0;negSampleTrain = 0
    allSampleTest = 0;posSampleTest = 0;negSampleTest = 0
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
        elif line.find('all') != -1:
            allPoint = line.find('all')
            posPoint = line.find('pos')
            negPoint = line.find('neg')
            allSample = int(line[allPoint + 5:line.find(',')].strip())
            posSample = int(line[posPoint + 5:line.rfind(',')].strip())
            negSample = int(line[negPoint + 5:].strip())

            if trainTag:
                allSampleTrain = allSample
                posSampleTrain = posSample
                negSampleTrain = negSample
                trainTag = False
            else:
                allSampleTest = allSample
                posSampleTest = posSample
                negSampleTest = negSample

    data = {'train_auc': train_auc, 'test_auc': test_auc,
            'featureKey': featureKey, 'featureImportance': featureImportance,
            'allSampleTrain': allSampleTrain, 'posSampleTrain': posSampleTrain, 'negSampleTrain': negSampleTrain,
            'allSampleTest': allSampleTest, 'posSampleTest': posSampleTest, 'negSampleTest': negSampleTest}

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


def ajaxGetFeatureName(request):
    import os
    data = {}
    BASE_DIR = '/home/tina/zhuyuting/毕设_20200108备份/毕设/实验数据'
    fileName = '17维原始特征20190701_20190707-20190710_cpo.txt'  # 这行传入实际的特征文件名

    BASE_DIR1 = '/home/tina/zhuyuting/bishe/jupyterProject/'

    if fileName.find("维") != -1:
        featureNum = int(fileName[0:fileName.find("维")])
        filePath = ''
        if featureNum == 17:
            if fileName.find('cpo') != -1:
                filePath = os.path.join(BASE_DIR1,'17_cpo.txt')
            else:
                filePath = os.path.join(BASE_DIR1, '17_comment.txt')
        else:# 34
            filePath = os.path.join(BASE_DIR1, '34_comment.txt')

        f = open(filePath)
        for line in f:
            feature = line[0:line.find(':')].strip()
            meaning = line[line.find(':') + 1:].strip()
            data[feature] = meaning
        for key in data:
            print(key)
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')

    else:  # 以不满意单个指标为标签的模型 现在未开发
        print('未找到文件！')
        return render(request, 'empty.html')





def empty(request):
    return render(request, 'featureTest.html')
