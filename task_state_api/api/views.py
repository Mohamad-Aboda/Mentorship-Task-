from http.client import ResponseNotReady
from typing import Reversible
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api

from .models import Task 
from .serializers import TaskSerializer
from api import serializers


def index(request):
    tasks = Task.objects.all()
    return render(request, 'api/index.html', {'tasks':tasks})


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializers.data)                   



@api_view(['POST'])
def taskUpdate(request, pk):
    task = get_object_or_404(Task, id = pk)
    serializer = TaskSerializer(instance=task, data = request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete() 

    return Response('Deleted')