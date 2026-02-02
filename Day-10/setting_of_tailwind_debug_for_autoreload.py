### To configure tailwind reload--- go to urls of project and write this code line to create the path

from django.conf import settings
if settings.DEBUG:
    urlpatterns+=[
        path("__reload__/",include("django_browser_reload.urls"))
    ]

### Now to debug the reload--go to settings of project and after installed app section and after middleware section write this if logic

## Installed app

if DEBUG:
    INSTALLED_APPS+=['django_browser_reload',]

## Middleware 

if DEBUG:
    MIDDLEWARE+=["django_browser_reload.middleware.BrowserReloadMiddleware",]

### Then run there tailwind-- pyhton manage.py tailwind start and then run the server pyhton manage.py runserver
