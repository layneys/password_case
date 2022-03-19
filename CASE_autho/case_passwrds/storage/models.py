from django.db import models

# Create your models here.

class Case(models.Model):
    project_name = models.CharField(max_length=100, default='')
    login = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')