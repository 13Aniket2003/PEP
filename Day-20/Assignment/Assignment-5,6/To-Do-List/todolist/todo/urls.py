from django.urls import path
from .views import login_view,signup_view, HomeView, TodoDetailView,logout_view
from django.urls import path, include
from .views import SignupViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Signup', SignupViewSet)

urlpatterns = [
    path("login/",login_view,name='login'),
    path("",signup_view,name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('list/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path("logout/", logout_view, name="logout"),
    path('rest/',include(router.urls)),
]





