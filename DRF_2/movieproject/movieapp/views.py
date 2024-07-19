from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response

@api_view(["GET", "POST"])
def get_all_movies(request):

    if request.method=="GET":
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
@api_view(["GET", "PUT", "DELETE"])
def edit_delete_movies(request, pk):

    try:
        movie=Movie.objects.get(pk=pk)
    except:
        return Response("Movie not found")

    if request.method=="GET":
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method=="DELETE":
        movie.delete()
        return Response(f'{movie} has deleted.')
    
    return Response(serializer.error)