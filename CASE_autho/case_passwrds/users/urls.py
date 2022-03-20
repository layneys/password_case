from django.urls import path
from . import views
# from django.contrib.auth import

app_name = 'users'


urlpatterns = [
    # post views
    # path('login/', views.LoginView.as_view(), name='login'),
    path('getjson/', views.LoginView.as_view(), name='getjson'),
]