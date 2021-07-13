from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
def index(request):
    return HttpResponse('OK')
# Create your views here.
def index_view(request):
    html='这是我的首页'
    return HttpResponse(html)

def page1_view(request):
    html1='这是我的第二页面'
    return HttpResponse(html1)
def pagen_view(request,pg):#必须要有参数
    intf='zhesfhdf%s'%(pg)
    return HttpResponse(intf)

def cal_view(request,a,b,c):#必须要有参数
    if b not in ['+','-','*','-.']:

        return HttpResponse('wrong')
    if b=='+':
        result=a+c
    elif b=='-':
        result=a-c
    elif b=='*':
        result=a*c
    elif b=='-.':
        result=a/c
    return  HttpResponse('结果是%s'%(result)) #result yaodai ()
