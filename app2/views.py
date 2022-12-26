from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun3(request):
    return HttpResponse('<h2> this is my first view in app2</h2>')
def fun4(request):
    return HttpResponse('<h2> this is my second view in app2</h2>')