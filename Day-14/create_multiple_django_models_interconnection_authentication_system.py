## today we have learned how to make multiple models and how to do interconnection between them

# 1. a. we create view page of a model which will render title and description and will store it in backend.
from django.shortcuts import render
from polls.models import FormModel
def form_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description=request.POST.get('description')

        data=FormModel(title=title,description=description)
        data.save()
    return render(request,'form.html')

# b. we create a model to run in backend and to store the input

class FormModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    # last_modified = models.DateTimeField(auto_now_add = True)
    # img = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.title

# 2.a. we create a login view page where user will give input for login and that will be stored in backend. 
# and also we connect it signup page such that it can redirect to singup page for new create account
# and after successful login it will redirect to home page of web

from django.template import loader
from django.shortcuts import render,redirect
from django.contrib import messages
from polls.models import LoginUser
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = None

        try:
            user = SignupUser.objects.get(username=username, is_active = True)
        except SignupUser.DoesNotExist:
            try:
                user = LoginUser.objects.get(username=username, is_active = True)
            except LoginUser.DoesNotExist:
                user = None
        else:
            if user and user.check_password(password):
                messages.success(request, f"Welcome, {username}")
                return redirect("home")
            messages.error(request, "Invalid username or password")       
    return render(request, "login.html")

# b. also we have created a model to store the i put of users in backend.
# and also to verify the authentication by comparing the input with the existing database of inputs to verify it

class LoginUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password:str)->None:
        """Hash and set a raw password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password:str)->bool:
        return check_password(raw_password, self.password)    
    
    def save(self, *args, **kwargs):
        # ensure stored password is always hashed once
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)     

    def __str__(self):
        return self.username

# 3. a. we create a sigpup view page where user will give inputs for signup and database ill store the input to authenticate it in login page
# also we have connect the signup page with login page such that after successful signup it will redirect to login page

from django.template import loader
from django.shortcuts import render,redirect
from django.contrib import messages
from polls.models import SignupUser

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        password = request.POST.get('password')


        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif SignupUser.objects.filter(username = username).exists():
            messages.error(request, "Username already taken")
        elif SignupUser.objects.filter(email = email).exists():
            messages.error(request, "Email already registered.")        
        else:
            new_user = SignupUser(username = username, email = email)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, "Signup successful. you can now log in")
            return redirect("login")
        
    return render(request, "signup.html")

# b. also we have created a model to store the i put of users in backend.
# and also to verify the authentication tp compare the input which will be given by user in login page.

class SignupUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)
    
    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


        login_user, _ = LoginUser.objects.get_or_create(username = self.username)
        login_user.password = self.password
        login_user.is_active = self.is_active
        login_user.save()

    def __str__(self):
        return self.username

# 4. Then we put the link of path for all the views

from django.urls import path
from . import views
#from .views import home_view,form_view,login_view -----> if we declare here the views name
urlpatterns=[
    path("polls/",views.index,name="index"),
    path("home/",views.home_view,name="home"),
    path("registration/",views.registration,name='registration'),
    path("form",views.form_view,name="form"),   #----> no need to write views. here cause its declared earlier write only form_view
    path("login/",views.login_view,name='login'),
    path("",views.signup_view,name='signup'),
]

# 5. Then we register our model in admin and we do makemigration then migrate and runserver to run it

from django.contrib import admin

# Register your models here.
from .models import users,FormModel,LoginUser,SignupUser
admin.site.register(users)

admin.site.register(FormModel)

admin.site.register(LoginUser)

admin.site.register(SignupUser)

# note:- to see the webpages of signup, login, home we created html file and we linked it for redirect accordingly needs.