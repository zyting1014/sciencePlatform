from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cpoModel.urls')),
    re_path('(.*?)', views.errorHtml),
]

