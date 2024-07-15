from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def get_all_tasks(request):
    if request.method=="GET":
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])
def edit_delete_tasks(request, pk):
    try:
        tasks=Task.objects.get(pk=pk)
    except:
        return Response("Task not found")
    
    if request.method=="GET":
        serializer=TaskSerializer(tasks)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=TaskSerializer(tasks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=="DELETE":
        tasks.delete()
        return Response({"message":f'{tasks} has deleted'})
    
    return Response(serializer.errors)
