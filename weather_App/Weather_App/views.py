from django.shortcuts import render,redirect
import requests
from decouple import config
from pprint import pprint
# Create your views here.
def index(request):
    
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    city="istanbul"
    response=requests.get(url.format(city,config('API_KEY')))#url'e istek atıyoruz.
    content=response.json()
    pprint(content)
    return render(request,'Weather_App/index.html')