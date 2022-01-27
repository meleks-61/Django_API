from dataclasses import fields
from .models import Flight,Reservation,Passenger
from rest_framework import serializers

class FligtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields="__all__"
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields="__all__"
        
class ReservationSerializer(serializers.ModelSerializer):
    passenger=PassengerSerializer(many=True,required=False)#birden çok passenger bilgisini dtabase create edebilir
    flight_id=serializers.IntegerField()
    user=serializers.StringRelatedField()#,readonly-user modelinin str fieldi neyse onu döndürür(username)
    user_id=serializers.IntegerField(required=False,write_only=True)#(get içe çekerken kullanmak istemiyorum,sadece create,post vs için kullanmak istiyorum.Hangi reservationa ail bilgi oldugunu belirleyebilmem için
    
    class Meta:#modelserializer old için bunu yazmak zorundsyız
        model=Reservation
        fields=(
            "id",
            "flight_id",
            "passenger",
            "user",
            "user_id",
        )
    
    def create(self,validated_data): #bana gelen veriler validate edip Pythonun işleyebileceği hale getiriyoruz.Bir array içinde dictler[{},{},{}..]
       passenger_data=validated_data.pop('passenger')#burda kullanıcıdan gelen passenger aslında içinde dictler olan bir liste,pop ile biz bu bilgiyi original listeden(validated_datadan) kaldırıyoruz ama passenger_data bu bilgiyi(passenger arrayini) tutuyor 
       validated_data["user_id"]=self.context['request'].user.id#burdaki context bir dict ve modelviewset(class base ) kullandıgım için bana serializer içinde otomatik geliyor  geliyor#(reservation bilgilerinde user_id yok ama bana lazım)normalde validated_data bir dictionary ve ben bu dicte "user_id"diye bir değişken koyuyorum.user_id yi token a göre sorguladı
       reservation=Reservation.objects.create(**validated_data)#user_id ve flight_id ile reservation create ettik.
       for passenger_d in passenger_data:
            reservation.passenger.add(Passenger.objects.create(**passenger_d))#manttomany fieldına bir şey eklemek istiyorsak bunu add ile yapıyoruz
       reservation.save() 
       return reservation   