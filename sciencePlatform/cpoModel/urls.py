from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('comment/',views.comment,name='comment'), # 用户满意度数据
    path('mainModel/',views.mainModel,name='mainModel'), # 主模型配置
    path('empty/',views.empty,name='empty'), # 空网页
    path('ajaxGetModel/',views.ajaxGetModel,name='ajaxGetModel') # ajax get方法 获取模型标题表格
 ]
