from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo<h1><center>')

@api_view(['GET'])#Httpresponsedan bana sadece GET gelirse cevap veririm, başka hiçbirtürlü cevap vermem
def todoList(request):
    query=Todo.objects.all()
    serializer=TodoSerializer(query,many=True)#queryset formatında gelen To modeline ait elemanların bilgisini json formatına dönüştürmek için<-:
    return Response(serializer.data)#bizim şuan frontentle işimiz yok o yüzden template gerek yok,biz sadece api olusturuyoruz oyüzden serializer değişkeni içine atadıgımız json formatındaki bilgiden bizim işimize yarayacak olan data kısmını alıyoruz.
@api_view(['POST'])
def todoListCreate(request):
    serializer=TodoSerializer(data=request.data)#gelen verileri(request.data) python objesine çevirdi
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','POST'])
def todo_List(request):
    if request.method=='GET':
        query=Todo.objects.all()
        serializer=TodoSerializer(query,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])#update
def todoList_Update(request,pk):
    query=Todo.objects.get(id=pk)
    serializer=TodoSerializer(instance=query,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    