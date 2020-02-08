from django.shortcuts import render

def errorHtml(response,errMsg):
    return render(response, 'index.html')

