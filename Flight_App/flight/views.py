from django.shortcuts import render
from .models import Flight,Reservation,Passenger
from .serializers import FligtSerializer,ReservationSerializer,StaffFlightSerializer
from rest_framework import viewsets,filters#viewsetsi modelviewset kullanavağız,filter da search için
from .permissions import IsStuffOrReadOnly



# Create your views here.
class FlightView(viewsets.ModelViewSet):#tüm işlemleri(get,put,post,delete,patch,head)yapıyor ModelViewset
    queryset=Flight.objects.all()
    serializer_class=StaffFlightSerializer#FligtSerializer
    permission_classes=(IsStuffOrReadOnly,)#permission tanımlamalıyım.Admin ise,bu işlemleri yapacak kişi ise create,update işlemlerini yapsın ,onun haricinde kim varsa;authenticated olsun veya olmasın sisteme giren kişiler sadece read (flightları görebilsin).Her girenin create Update yapmaması lazım
    filter_backends=(filters.SearchFilter,)#search için
    search_fields=('departureCity','arrivalCity','dateOfDeparture')#search için
    
    def get_serializer_class(self):#iki ayrı serializer arasında switch yapmamı sağlar
        if self.request.user.is_staff:
            return super().get_serializer_class()#queryset
        else:
            return FligtSerializer
    
class ReservationView(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer  
    
    def get_queryset(self):#kullanıcı is_staff ise bütün rezervasyonlatı görsün is_staff değilse görmesin istiyorum.Bunun için querysete bir condition yazmam lazım(bunun için get_queryset methodunu overright ediyoruz)eğer overright işlemi varsa super ile alıyoruz veriyi(pythonun object orianted olması ile ilgili bir durum bu)
        queryset=super().get_queryset()#resercationview deki queryseti bize döndürüyor
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
    

