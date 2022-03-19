from django import forms


class InfoForm(forms.Form):
    project_name = forms.CharField(max_length=100)
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)