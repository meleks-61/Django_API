from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    flightNumber=models.IntegerField()
    operatingAirlines=models.CharField(max_length=25)
    departureCity=models.CharField(max_length=30)
    arrivalCity=models.CharField(max_length=30)
    dateOfDeparture=models.DateField()#hangigün kalkacak
    estimatedTimeOfDeparture=models.TimeField()#ogün hangi saatte kalkacak
    
    def __str__(self):
        return f"{self.flightNumber} - {self.departureCity} - {self.arrivalCity}"
    
class Passenger(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=60)
    email=models.EmailField()
    phoneNumber=models.IntegerField()
    updatedDate= models.DateTimeField(auto_now=True)
    createdDate=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstName} - {self.lastName}"
    
class Reservation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)#o rezervasyonu hangi user login olarak yapmıs.Bir User birden çok kişi için rezervasyon yaptırabilir ama bir rezervasyonun bir tane userı olur
    passenger=models.ManyToManyField(Passenger,related_name='passenger')#bir yolcunun birden cok rezervasyonu(farklı zamanlarda ) olabilir ,bir rezervasyonda birden cok yolcu olabil oyuzden many to many
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE,related_name='reservations')
    
    def __str__(self):
        return self.flight
    