from app1.views import *
from django.urls import path

app_name='akil'
urlpatterns=[
    path('akil/',akil,name='akil'),
]
