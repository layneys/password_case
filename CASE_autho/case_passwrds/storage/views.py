from django.shortcuts import render
from .forms import InfoForm
import os
import json
import requests

from cryptography.fernet import Fernet

from .models import Case
from django.shortcuts import redirect
# Create your views here.
script_dir = os.path.dirname(__file__)
from .booba import data

with open("pubkey", "r") as rfile:
    public_key = rfile.readline()

def index(request):
    project_name = ''
    login = ''
    password = ''
    public_cipher = Fernet(public_key)

    def ciph_gen(depassword):
        return public_cipher.encrypt(depassword)

    def ciph_degen(enpassword):
        return public_cipher.decrypt(enpassword)

    form = InfoForm(request.POST or None)

    if form.is_valid():
        path_name_user = request.user.username
        project_name = form.cleaned_data.get("project_name")
        login = form.cleaned_data.get("login")
        password = form.cleaned_data.get("password")

        password = ciph_gen(password)

        # path = f'{project_name}'
        #
        # isExist = os.path.exists(path)
        #
        # if not isExist:
        #     os.mkdir(project_name) #mkdir
            # with open(os.path.join(script_dir, f'../{project_name}/.txt'), 'w') as psina:
            #     psina.writelines(login + '\n' + password)
        # else:
        #     with open(os.path.join(script_dir, f'../{project_name}/psina.txt'), 'a') as psina:
        #         psina.writelines('\n' + login + '\n' + password)

        isExist = os.path.exists("storage/" + path_name_user + ".json")

        if not isExist:
            with open("storage/" + path_name_user + ".json", "w") as write_file:
                write_file.write("{}")

        with open("storage/" + path_name_user + ".json", "r") as read_file:
            data = json.load(read_file)
            data.update({f'{project_name}' : {f"{login}" : f'{password}'}})
        with open("storage/" + path_name_user + ".json", "w") as write_file:
            json.dump(data, write_file)

    context = {
        "form": InfoForm,
    }

    return render(request=request, template_name='storage.html', context=context)