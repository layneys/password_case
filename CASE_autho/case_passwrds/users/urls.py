from django.contrib import admin
from django.urls import path
from .views import UserCreateView, index
app_name = 'users'
urlpatterns = [
    path('registration/',  UserCreateView.as_view(), name='user_create',),
    path('',  index, name='index_page',)

]
