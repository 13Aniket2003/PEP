## Create a folder name django_project and then create a project inside it named New_project and create an app name portfolio

# portfolio cmd
django-admin startapp portfolio

# new_project cmd
django-admin startproject new_project django_project

## Then create a folder name inside that djange_project named templates and static

## Inside the templates create file named about.hmtl,index.html and contact.html

## Inside static create named style.css
# we made a file name static for storing css file such that in further future,
#  when big project will made that time loading to html file directly will be too much pressure.
# So by creating a different file it will be fast and easy to access,
#  also during changes in setting or html code as css file is differ for that reason the changes in html file will not affect css file.

## now design the html and css 

## After that link the css file by using "{% load static %}" and "<link rel="stylesheet" href="{% static 'style.css' %}">"

## Now after creating the html and css file we have to do some changes inside the New_project

## In new_project app open setting.py and there change the build path inside the project section

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]

## then in template section of setting.py of new_project change the 'DIRS' section and add templates (the new file name we created for html)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],   #----------------> only this is change rest all remain same
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

## then create a file named urls.py in both new_project and portfolio

## then create file name view.py inside the project and create a file name urls.py inside the app

## now configure the urls.py for both project and app

# portfolio

from django.urls import path
from . import views
urlpatterns = [
    path("",views.portfolio_index,name="portfolio_index"),
]

# project

from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("portfolio/",include("portfolio.urls")), #-----> creating path for url to run and switch between pages after run through local host port
    path("admin/", admin.site.urls),
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('service/',views.service,name='service'),
    path('project/',views.project,name='project'),
    path('feedback/',views.feedback,name='feedback'),
]

## now configure the views.py for both project and app

# project

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request,'index.html')    #-----> to show the html or webpage use render(request,"file_name.html")

def contact(request):
    return HttpResponse("This is contact page")   #-----> to show the message of page use httpresponse

def about(request):
    return render(request,'about.html')

def service(request):
    return HttpResponse("Raise query for service")

def project(request):
    return HttpResponse("Below are the projects build till now")

def feedback(request):
    return HttpResponse("Don.t forget to give your valuable feedback here")

## now run the project 

# run cmd

# 1. first migrate
python manage.py migrate 

# 2. then run server
python manage.py runserver

# To switch between the pages of templates (index,contact,about)use "/index or /about or /contact" after the local host port "8000"

http://127.0.0.1:8000 ---> /about or /contact
#---------------------------------------------------------------------------------------------------------------------------------------------