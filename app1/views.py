from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun1(request):
    return HttpResponse('my first view in app1')
def fun2(request):
    return HttpResponse('<h1>my second view in app1</h1>')


