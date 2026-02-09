from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("info/",views.info,name="info"),
    path("layout/",views.layout,name="layout"),
    path("jinja/",views.jinja_page,name="jinja"),
]
