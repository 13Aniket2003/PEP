from django.urls import path
from .views import HomeView, TodoDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
