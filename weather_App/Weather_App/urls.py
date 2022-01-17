from django.urls import path
from .views import index,delete_weather

urlpatterns = [
    
    path('',index,name='index' ),
    path('delete/<id>',delete_weather,name='delete' ),
]