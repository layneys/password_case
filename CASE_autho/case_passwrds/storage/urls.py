from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'storage'

urlpatterns = [
    path('', index, name='index_page'),
]
