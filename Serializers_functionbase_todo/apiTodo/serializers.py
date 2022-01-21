from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    todo_detail=serializers.HyperlinkedIdentityField(view_name='todo-detail')#apideki verilerin yanında bir link olsun ve oraya tıkladıgımda verinin detail syfasına yönleneyim:)
    class Meta:
        model=Todo
        #fields="__all__"(HyperlinkedIdentityField için all seçneğini)
        fields=(
            'id',
            'task',
            'description',
            'priority',
            'done',
            'todo_detail'
        )
        
        
        
        
    