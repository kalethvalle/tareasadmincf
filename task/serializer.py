from rest_framework import serializers
from .models import TaskManager, Prefijo

class TaskManagerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TaskManager
        fields = '__all__'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'

class PrefijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prefijo
        fields = '__all__'
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
