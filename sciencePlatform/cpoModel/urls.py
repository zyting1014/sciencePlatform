from django.urls import path
from . import view

urlpatterns = [
    path('index/', view.index),
]
