### taking input from users to update the database without operating via python.shell

## creating a form in form.py inside the app to take input from users 

from django import forms

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())

## then we create a model to make the form and to store the form

class users(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    # addresse=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    # phone_number=models.CharField(max_length=15)
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"
    
## then in admin.py we register our model

from django.contrib import admin
from .models import users
admin.site.register(users)

## to view the form we go to views.py and render it

from django.shortcuts import render
from .forms import InputForm

def home_view(request):
    context={}
    context['form']=InputForm()
    return render(request,"registartion.html",context)

## then in urls.py we create the path to view

path("home/",views.home_view,name="home"),


## now again we create another model named FormModel to store input in models in backend
    
class FormModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    # last_modified = models.DateTimeField(auto_now_add = True)
    # img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title

## then in admin.py we register our model

from django.contrib import admin
from .models import users,FormModel
admin.site.register(users)
admin.site.register(FormModel)

## then we create the view page of database in views.py

## 1. GET method

from django.db import models

# def form_view(request):
#     print(request.GET)
#     return render(request, "form.html")

## 2. POST method

# from django.shortcuts import render
# def form_view(request):
#     if request.method == "POST":
#         print(request.POST)
#         first__name = request.POST.get('first__name')
#         last__name=request.POST.get('last__name')
#         email_address=request.POST.get('email_address')
#         phone_number=request.POST.get('phone_number')
#     return render(request, "form.html")

## now as we create database in python shell, so without use of python shell to store and update the inputs of users in model in admin
##---> we write this method

## using POST method

from django.shortcuts import render
from polls.models import FormModel
def form_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description=request.POST.get('description')

        data=FormModel(title='title',description='description')
        data.save()
    return render(request,'form.html')

## Also we have created all the html file what we need to show in templates section and we linked it.

## now to run the server we have to write the following cmds--->

## 1. first to migrate all the changes in database we write-->

python manage.py makemigrations

## 2. then we do migrate and then we run the server

## sometime the migration or integration fails or we change some file and that time it does not works or doesnot integrate
## That time inside the app--> inside migration folder--> there will be some migrated file named "0001_initial.py", then
## "0002_'something'.py", etc... this are the updates or changes we have done in migration but due to changes something 
## it fails to fecth the original data we want that time we have to delete all the files except '0001 initial.py' 
## then we have to run this cmd-->

python manage.py makemigrations polls #----> that app name will be there at last cause we want to migrate only the app not whole the project cause the integration of app is not wokring

## then again do migration and run the server.
