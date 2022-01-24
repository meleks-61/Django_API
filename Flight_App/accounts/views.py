from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView#register işleminde kullanıcı sadece post gönderdiğinden bu işlem için sadece createapi importu yeterlidir



# Create your views here.
class RegisterApi(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    #user create edildiğinde bize kullanıcı bilgileri dönmesinde mesj dönsün istiyorum,genericten aldıgımız CreateApiview indeki post methodunu overright edeceğiz
    
