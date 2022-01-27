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
    

