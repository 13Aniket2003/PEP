## make another project name Slug and inside that make a app Slugapp
## then in settings.py created database

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

## created a model

from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("artical_detail", args = [str(self.id)])

## registered in admin.py 

from django.contrib import admin
from .models import Article

admin.site.register(Article)