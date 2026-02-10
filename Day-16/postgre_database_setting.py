## write code under setting.py of project to link postgre database with python by commenting the default dbsql database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'aniket',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## configuration of apps.py of app to set the app

from django.apps import AppConfig
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

## configuration of default auto field under settings.py

default_auto_field = 'django.db.models.BigAutoField'

## creating model in models.py and registering it inside admin.py

class student(models.Model):
    name = models.TextField()
    enr_num = models.IntegerField()
    course = models.TextField()
    sem = models.IntegerField()
    section = models.TextField()

class info(models.Model):
    enr_num= models.ForeignKey("student", on_delete=models.SET_NULL, null=True)
    stu_name=  models.TextField()
    father_name =  models.TextField()
    mother_name =  models.TextField()
    addr =  models.TextField()
    ph_no =  models.IntegerField()
    email =  models.TextField()

# registering

from django.contrib import admin
from .models import info, student

admin.site.register(info)
admin.site.register(student)

