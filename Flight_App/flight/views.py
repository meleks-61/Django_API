from django.shortcuts import render
from .models import Flight,Reservation,Passenger
from .serializers import FligtSerializer,ReservationSerializer
from rest_framework import viewsets#modelviewset kullanavağız
from .permissions import IsStuffOrReadOnly



# Create your views here.
class FlightView(viewsets.ModelViewSet):#tüm işlemleri(get,put,post,delete,patch,head)yapıyor ModelViewset
    queryset=Flight.objects.all()
    serializer_class=FligtSerializer
    permission_classes=(IsStuffOrReadOnly,)#permission tanımlamalıyım.Admin ise,bu işlemleri yapacak kişi ise create,update işlemlerini yapsın ,onun haricinde kim varsa;authenticated olsun veya olmasın sisteme giren kişiler sadece read (flightları görebilsin).Her girenin create Update yapmaması lazım

class ReservationView(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer  
    
    def get_queryset(self):#kullanıcı is_staff ise bütün rezervasyonlatı görsün is_staff değilse görmesin istiyorum.Bunun için querysete bir condition yazmam lazım(bunun için get_queryset methodunu overright ediyoruz)
        queryset=super().get_queryset()#resercationview deki queryseti bize döndürüyor
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
    

