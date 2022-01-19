from django.urls import path
from .views import home,todoList,todoListCreate

urlpatterns = [
    path('',home ),
    path('todoList/',todoList),
    path('todoListCreate/',todoListCreate),
]