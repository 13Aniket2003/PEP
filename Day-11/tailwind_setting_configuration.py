### After installation of tailwind we have to configure the patha nd urls.
### To configure it----> first go to theme folder and go to urls.py
### and change add this. Also we made an Error 404 html page
### Suc that whenever any error ocuur it will show this custom
### HTML page not default page and we also create the path for it.

from django.urls import path
from . import views
urlpatterns = [
    path('tailwind',views.index,name='index'),
    path('404',views.error,name='404'),
]
#----------------------------------------------------------------

### After that---> go to views.py and add this for both tailwind and error 404 to view it.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'base.html')
def error(request):
    return render(request,'404.html')
#---------------------------------------------------------

### Now in main project---> go to urls.py and in the urlpatterns section
### add this urls path means include its path to show.

urlpatterns = [
    path("",include("theme.urls")),
    ]
#------------------------------------------------------

### Now go to setting.py in main project and allow the security host for up-changes.

DEBUG = False
ALLOWED_HOSTS = ['*']
#----------------------------------------------------------------

### to create a project outside of venv but remaining partially in it like creating an project and app inside PEP/Day-11 the command is--->

## for making project

python -m django startproject main project  # not for all time but whenever any issue occur during creat try this (optional)

## for making apps

python -m django startapp home # same as above (optional)
