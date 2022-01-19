from django.urls import path
from .views import home,todoList,todoListCreate,todo_List

urlpatterns = [
    path('',home ),
    path('todoList/',todoList),
    path('todoListCreate/',todoListCreate),
    path('todo_List/',todo_List),
]