from django.shortcuts import render,redirect,get_object_or_404
import requests
from decouple import config
from pprint import pprint
from .models import City
import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    cities=City.objects.all()
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    g_city=request.GET.get("city")#Post methoduyla göndermedik çünkü post ile gönderseydik direk database kaydedeceği için sıkıntı yaşayabilirdik var olan bir şehri tekrar kaydedebilirdi.Ama get ile alıp önce var mı yokmu diye sorgulatıp sonra kaydediyoruz
    #print(g_city)
    if g_city:#none dönmesini engellemek için(boş arattıgımda)
        response=requests.get(url.format(g_city,config('API_KEY')))
        if response.status_code==200:#istek atılan isimde bir şehir mevcut ise 200 döner çünkü
           #responsedan dönen name i database kaydetmek istiyorum çünkü kendi yazdıgım city nin karakterleri dile göre değişiklik gösterebilir
            content=response.json()
            a_city=content["name"]
            if City.objects.filter(name=a_city):
                messages.warning(request,"This city already exist!")
            else:
                City.objects.create(name=a_city)
                messages.success(request,"City was successfully added")
        else:
            messages.warning(request,"There isn't a city called this name")
        return redirect("index")
    else:
        messages.warning(request,"Please enter a City")
    city_data=[]
    day=datetime.date.today()
    for city in cities:
        response=requests.get(url.format(city,config('API_KEY')))#url'e istek atıyoruz.
        content=response.json()
        #pprint(content)
        data={
            "city":city,
            "temp":content["main"]["temp"],
            "desc":content["weather"][0]["description"],
            "icon":content["weather"][0]["icon"],
            "day":day
            
                
              }
        city_data.append(data)
    #print(city_data)
    context={
        "city_data":city_data
    }
        
        
   
    return render(request,'Weather_App/index.html',context)

def delete_weather(request,id):
    city=get_object_or_404(City,id=id)
    city.delete()
    return redirect("index")

