from django.urls import path
from .views import home,todoList,todoListCreate,todo_List,todoList_Update,todoListDelete,todoList_Detail,TodoList,TodoDetail

urlpatterns = [
    # path('',home ),
    # path('todoList/',todoList),
    # path('todoListCreate/',todoListCreate),
    # path('todo_List/',todo_List),
    # path('todoList_Update/<int:pk>/',todoList_Update),
    # path('todoListDelete/<int:pk>/',todoListDelete),
    # path('todoList_Detail/<int:pk>/',todoList_Detail),
    
    path('todo-List',TodoList.as_view()),
    path('todo-Detail/<int:pk>',TodoDetail.as_view())
]