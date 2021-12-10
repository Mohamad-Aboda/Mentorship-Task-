from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task 
from .serializers import TaskSerializer


def index(request):
    tasks = Task.objects.all()
    return render(request, 'api/index.html', {'tasks':tasks})




# create & list  
@api_view(['POST', 'GET'])
def task_Create_List(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)                   
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)



#  Update & Delete & Delete 
@api_view(['PUT', 'GET', 'DELETE'])
def task_Update_Detail_Delete(request, pk):
    if request.method == 'PUT':
        task = Task.objects.get(pk = pk)
        serializer = TaskSerializer(instance=task, data = request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tasks = Task.objects.get(pk=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        task = Task.objects.get(id=pk)
        task.delete() 
        return Response('Task Deleted Succefully.')


@api_view(['POST'])
def change_state(request):
    task = Task.objects.filter(
        state = request.data['state']
    )


    req_state = request.data['state']
    queryset = Task.objects.all()
    giv_state = queryset.state 

    if (giv_state == 'active' and req_state == 'draft') or (giv_state == 'done' and req_state == 'draft')or (giv_state == 'draft' and req_state == 'done')or (giv_state == 'archived' and req_state == 'done') or (giv_state == 'archived' and req_state == 'active') or (giv_state == 'archived' and req_state == 'draft'):
        return Response('Invalid State!')
    else:
        task.state = req_state
        task.save()





