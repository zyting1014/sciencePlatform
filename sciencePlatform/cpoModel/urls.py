from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'), # 首页
    path('comment/',views.comment,name='comment'), # 用户满意度数据
    path('empty/',views.empty,name='empty'), # 空网页
 ]
