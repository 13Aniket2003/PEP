# #  to create a django file use this command ---> django-admin startproject project_name file_name
# #  to run djnago server first run the migrate by this command ---> pyhton manage.py migrate ---> here only every changes will occur or 
# # i can manage multiple file or projects ---> then run the server ---> python manage.py runserver --> and it will redirect to local host

# ### Adding polls app in django

# from django.apps import AppConfig
# class PollsConfig(AppConfig):
#     name = 'polls'

# ### adding url of polls to django to run

# from django.urls import path
# from . import views
# urlpatterns=[
#     path("",views.index,name="index"),
# ]
# #-------------------------------------------------------------------------------------------------------------------------------------------------

# ### creating view page of polls to view on server

# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello world !! you have done it")
# #----------------------------------------------------------------------------------------------------------------------------------------------------

# ### inserting the app name inside the setting of practice_project of django to make it new
# ## inside of Application definition there is installed app just write there polls to add

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'polls', #------> like this way here in above things are written already
# ]
# #--------------------------------------------------------------------------------------------------------------------------------------------------

# ### setting the url of practice_project to make it visible on server

# from django.contrib import admin
# from django.urls import include, path
# urlpatterns=[
#     path("polls/", include("polls.urls")),
#     path("admin/",admin.site.urls),
# ]
# #----------------------------------------------------------------------------------------------------------------------------------------------------