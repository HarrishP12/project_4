from app.views import *
from django.urls import path

app_name='akil'
urlpatterns=[
    path('akil/',akil,name='akil'),
]
