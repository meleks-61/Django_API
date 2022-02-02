from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
#endpointte bana category name dönsün(id) de olabilir;o category de kaçtane quiz oldugunu göstermek istiyoruz
class Category(generics.ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()