from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    priority = PrioritySerializer(read_only=True) 

    class Meta:
        model = Task
        fields = '__all__'
