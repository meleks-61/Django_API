from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView#register işleminde kullanıcı sadece post gönderdiğinden bu işlem için sadece createapi importu yeterlidir
from rest_framework.response import Response



# Create your views here.
class RegisterApi(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    #user create edildiğinde bize kullanıcı bilgileri dönmesinde mesj dönsün istiyorum,genericten aldıgımız CreateApiview indeki post methodunu overright edeceğiz
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)#serializer classında hangi serializerı belirttiysek onu döndürüyor(burada REgisterSerializer)
        #serializer=RegisterSerializer(data=request.data) yukarıdakinin yerine kullanılabilir bir alternatif
        serializer.is_valid(raise_exception=True)#valid değilse hata döndür 
        serializer.save()
        return Response({
            "message":"User successfully created."
        })
        #eğer her register olana bir token oluşturmak isteseydik burda(post methodunda) işlem yapacaktık ama bizim kullandıgımız login ve logout modellerinde token otomattik olarak olusturulup silindiği için gerek kalmadı