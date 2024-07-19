from django.shortcuts import render
from rest_framework import status, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from rest_framework.decorators import action
from .models import Post, Profile
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    @action(detail=True, methods=["post"])
    def register(self, request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            profile=Profile(user, user_type=request.data["user_type"])
            profile.save()
            return Response({"user":user, "profile":profile, "message":"signup successfull"}, status=status.HTTP_201_CREATED)
        
    @action(detail=True, methods=["post"])
    def login(self, request):
        username=request.data["username"]
        password=request.data["password"]
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return Response({"message":"username or password is wrong"}, status=status.HTTP_401_UNAUTHORIZED)
        
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    # @action(detail=True, methods=["post"])
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)