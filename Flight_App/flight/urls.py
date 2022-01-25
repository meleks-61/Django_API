from django.urls import path
from .views import FlightView
from rest_framework import routers#viewsetlerle çalışırken router kullanıyroduk


router=routers.DefaultRouter()
router.register('flights',FlightView)#filght/flights dediğimizde FlightViewini çalıştıracak.




urlpatterns = [
   
]
urlpatterns += router.urls#include ile de yapabiliriz böyle de yapabiliriz.
