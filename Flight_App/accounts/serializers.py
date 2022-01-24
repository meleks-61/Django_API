
from rest_framework import serializers,validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())],#emailimiz uniq olsun istediğimizden        
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type":"password"}#passwordün yıldızlı görünmesi için
    )
    password2=serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type":"password"}
        
        
    )
    #password2 user da yok ve email ile passwordun bazı özelliklerini burda tekrar tanımlayacagız .
    class Meta:
        model=User
        fields=["username",
                "first_name",
                "last_name",
                "email",
                "password",
                "password2",
        ]
        #kullanıcıın girdiği password ve password2 bilgilerini tekrardan döndürmek,ekrana yazdırmak olmaz.BU durumu burda extra_kwargslarla belirtebiliriz
        
        extra_kwargs={
            "password":{"write_only":True},
            "password2":{"write_only":True}
            
        }
        #User modelinde normalde password2 yok o yüzden create methodunu tekrar overright edip passsword2 yi içinden çıkaracağız
        
    def create(self,validated_data):
        password=validated_data.get("password")    
        validated_data.pop("password2")#kullanıcıdan gelen valide edilmiş password2 yi passworde atadagımız datdan cıkarıyoruz.Şuan bizim validated _datamız user create etmeye uygun hale geldi
        
        user=User.objects.create(**validated_data)#validated datadan userımızı create ettik
        user.set_password("password")#passwordlerimizi database açık olarak yazmamalıyız,bu işlem passwordu gizlemeyi sağlıyor
        user.save()
        return user
    
    #serializersmoselindeki iki fieldi (password,password2 yi kontrol edicez aynı mı değil mi diye) karşılaştıracağımızdan object validasyonunu kullanacağız serializerın
    def validate(self,data):#password1=password2 olmalı
        if data["password"]!=data["password2"]:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match."})
        return data
            