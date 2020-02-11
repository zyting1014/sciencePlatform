from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # 首页
    path('comment/', views.comment, name='comment'),  # 用户满意度数据
    path('mainModel/', views.mainModel, name='mainModel'),  # 主模型配置
    path('mainModelResult/', views.mainModelResult, name='mainModelResult'),  # 主模型配置
    path('dropRoute/', views.dropRoute, name='dropRoute'),  # 路线去重结果
    path('dValueEvaluation/', views.dValueEvaluation, name='dValueEvaluation'),  # 差值评估
    path('empty/', views.empty, name='empty'),  # 空网页

    path('ajaxGetModel/', views.ajaxGetModel, name='ajaxGetModel'),  # ajax get方法 获取模型标题表格
    path('ajaxGetTrainTestAuc/', views.ajaxGetTrainTestAuc, name='ajaxGetTrainTestAuc'),  # ajax get方法 获取模型auc&样本数
    path('ajaxGetFeatureName/', views.ajaxGetFeatureName, name='ajaxGetFeatureName')  # ajax get方法 获取特征名称
]


