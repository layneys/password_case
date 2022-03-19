from django.shortcuts import render
from .forms import InfoForm
import os
from .models import Case
from django.shortcuts import redirect
# Create your views here.
script_dir = os.path.dirname(__file__)
from .booba import data
def index(request):

    project_name = ''
    login = ''
    password = ''

    form = InfoForm(request.POST or None)
    if form.is_valid():
        project_name = form.cleaned_data.get("project_name")
        login = form.cleaned_data.get("login")
        password = form.cleaned_data.get("password")

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

        data[f'{project_name}'] = {
            f"{login}": f'{password}',
        }

    context = {
        "form": InfoForm,
    }

    return render(request=request, template_name='storage.html', context=context)