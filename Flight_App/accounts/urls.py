from django.urls import path,include
from .views import RegisterApi

urlpatterns = [
    path('auth/',include('dj_rest_auth.urls') ),#drf ile login (loginde token dönüyo)ve logout(login ile olusturulan tokeni otomait olarak siler) yapabiliyoruz
    path('register/', RegisterApi.as_view()),
    
]