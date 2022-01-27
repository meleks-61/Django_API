from django.urls import path
from .views import FlightView,ReservationView
from rest_framework import routers#viewsetlerle çalışırken router kullanıyroduk


router=routers.DefaultRouter()
router.register('flights',FlightView)#filght/flights dediğimizde FlightViewini çalıştıracak.Roter sayesinde bütün işlemler için(create,update,delete,detail için) bütün pathleri sağlıyor
router.register('resv',ReservationView)



urlpatterns = [
   
]
urlpatterns += router.urls#include ile de yapabiliriz böyle de yapabiliriz.
