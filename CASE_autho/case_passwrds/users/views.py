from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.views.generic import CreateView


class UserCreateView(CreateView):
    model = User
    form = UserCreationForm
    fields = ['username', 'email','password']
    template_name = 'auth/user_form.html'
    success_url = '/'

def index(request):
    return render(request, 'index.html')