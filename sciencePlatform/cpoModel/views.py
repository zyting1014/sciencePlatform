from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def comment(request):
    return render(request,'comment.html')

def empty(request):
    return render(request,'empty.html')

