from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('fun3/',fun3,name='fun3'),
    path('fun4/',fun4,name='fun4')
]