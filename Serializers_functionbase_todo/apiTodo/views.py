from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .serializers import TodoSerializer
from .models import Todo
#functionbase view için importlar
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#classbase viewlwr için importlar
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,mixins


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
        return Response(serializer.data)#başarılıysa update yaapr
    return Response(serializer.errors)#başarısızsa error döner

@api_view(['DELETE'])
def todoListDelete(request,pk):
    query=Todo.objects.get(id=pk)
    query.delete()
    return Response("Item deleted")
@api_view(['GET','PUT','DELETE'])
def todoList_Detail(request,pk):
    query=Todo.objects.get(id=pk)
    if request.method=='GET':
        
        serializer=TodoSerializer(query)
        return Response(serializer.data)
    elif request.method=='PUT':
        
        serializer=TodoSerializer(instance=query,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=='DELETE':
        
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
############################################## API_VIEW #################################################

class TodoList(APIView):#api view den inherit ediyoruzz
    def get(self,request):
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    def post(self,request):#create
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDetail(APIView):
    
    def get_object(self,pk):
        return get_object_or_404(Todo,pk=pk)
    def get(self,request,pk):
        todo=self.get_object(pk)
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    def put(self,request,pk):
        todo=self.get_object(pk)
        serializer=TodoSerializer(todo,data=request.data)
        if serializer.is_valid():
            #serializer._data["success"]="Todo successfully updated"#dataya eleman eklemek için
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        todo=self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#################### GEnericAPI View ###############
class TodoListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*kwargs,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*kwargs,**kwargs)

    
    

class TodoRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
        
       