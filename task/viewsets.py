from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import TaskManager, Prefijo
from .serializer import TaskManagerSerializer, PrefijoSerializer

class TaskManagerViewsets(viewsets.ModelViewSet):
    queryset = TaskManager.objects.all()#.order_by('id').reverse()[:1]
    serializer_class = TaskManagerSerializer 

class PrefijoViewsets(viewsets.ModelViewSet):
    queryset = Prefijo.objects.all()
    serializer_class = PrefijoSerializer 
