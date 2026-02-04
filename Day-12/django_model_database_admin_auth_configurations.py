
### Architecture of model-->views-->templates

#  --------------------------------------------------------------------------------------------
#  |                                                                                          |
#  |       ORM                         Business logic                    Display logic        |
#  |    ---------    datasets          ---------      data to display    ------------         |
#  |   | modles |  ---------------->   | views |    ------------------>  | templates |        |
#  |   |------- |  <----------------   |-------|    <------------------  |-----------|        |
#  |      |  |      CRUD operation         |            User input                            | 
#  |      |  |                             |                                                  |
#  |    ---------                      ----------                                             |
#  |    |   DB  |                      |  user  |                                             |
#  |    ---------                      ----------                                             |
#  |                                                                                          |
#  --------------------------------------------------------------------------------------------


## to register the model configure this code in models.py of the app

from django.contrib import admin
from .models import users
admin.site.register(users)
#---------------------------------------------------------------------

### write this code to configure the model in views.py of app

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import users

def registration(request):
    return render(request,"registration.html")

def index(request):
    myusers = users.objects.all().values()
    template = loader.get_template('user_list.html')
    context = {
        'myusers' : myusers,
    }
    return HttpResponse(template.render(context, request))
#----------------------------------------------------------
### write this code to configure the url path for the model in urls.py of app
from django.urls import path
from . import views
urlpatterns=[
    path("polls/",views.index,name="index"),
    path("",views.registration,name='registration'),
]
#-----------------------------------------------------------

### write this to create the model in models.py in app

from django.db import models
class users(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    # addresse=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    # phone_number=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
#------------------------------------------------------------------------------

### write this code in urls.py of project to create the path for the app

from django.contrib import admin
from django.urls import include, path
urlpatterns=[
    path("", include("polls.urls")),
    path("admin/",admin.site.urls),
]
#-----------------------------------------------------------------------

## to make a model write this in cmd

python manage.py makemigrations 

## then to create the admin authentication write this in cmd

python manage.py createsuperuser 

## to create dadabase or table of the model for user entry write this in cmd

python manage.py sqlmigrate polls 0001 

## to run the shell and to give input from user write this code in cmd

python manage.py shell  

## write thiscode to create the data base or table for user input entry

from polls.models import user
u=user(first_name='aniket',last_name='dutta',gmail='dutta@gmail.com')
u.save()
users.objects.all().values()
y=users.objects.all().values().get(id='value')
users.objects.get(id='value')
y['first_name']='ANIKET'
y_inst=y_inst[**y]
y_inst.save()
#-----------------------------------------------------------------------------
