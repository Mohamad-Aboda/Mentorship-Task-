from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Task 
from .serializers import TaskSerializer


# home page 
def index(request):
    return render(request, 'api/index.html', {})



# create task & list all tasks   
@api_view(['POST', 'GET'])
def task_create_list(request):

    ok = False
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


#check vaild or invalid update 
def check_valid_invaid_update(giv_state, req_state):
    ok = True
    if ((giv_state == 'active' and req_state == 'draft') or 
            (giv_state == 'done' and req_state == 'draft')or 
            (giv_state == 'draft' and req_state == 'done')or 
            (giv_state == 'archived' and req_state == 'done') or 
            (giv_state == 'archived' and req_state == 'active') or 
            (giv_state == 'archived' and req_state == 'draft')):
            ok = False

    # return True if valid update else return False 
    return ok 

#  Update task& Delete task & Detail of certain task 
@api_view(['PUT', 'GET', 'DELETE'])
def task_update_detail_delete(request, pk):
    # Update under predefined state machine
    if request.method == 'PUT':
        
        task_object = get_object_or_404(Task, pk=pk)
        giv_state = task_object.state

        data = request.data
        req_state = data['state']

        ok = check_valid_invaid_update(giv_state, req_state)
        
        if ok:
            serializer = TaskSerializer(instance=task_object, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response('Invalid Update You should follow the predefined state')


    # Detail
    elif request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)
    # Delete 
    elif request.method == 'DELETE':
        task = get_object_or_404(Task, pk=pk)
        task.delete() 
        return Response('Task Deleted Succefully.')



