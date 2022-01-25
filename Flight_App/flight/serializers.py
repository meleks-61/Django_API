from dataclasses import fields
from .models import Flight,Reservation,Passenger
from rest_framework import serializers

class FligtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"