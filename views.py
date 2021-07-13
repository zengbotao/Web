from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
def index(request):
    return HttpResponse('OK')
print('hello')
print('lel')
# Create your views here.
