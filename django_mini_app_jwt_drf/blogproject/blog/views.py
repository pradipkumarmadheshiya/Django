from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer, PostSerializer
from .models import Profile, Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
import jwt, datetime

class RegisterView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            profile=Profile(user=user, user_type=request.data["user_type"])
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")

        user=authenticate(request, username=username, password=password)
        if not user:
            raise AuthenticationFailed("user not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("check password")
        
        payload={
            "id":user.id,
            "exp":datetime.datetime.now(datetime.UTC)+datetime.timedelta(minutes=60)
        }
        jwtoken=jwt.encode(payload, "secret", algorithm="HS256")
        response=Response()
        response.set_cookie(
            key="jwtoken",
            value=jwtoken
        )
        response.data={"message":"login successful", "jwtoken":jwtoken}
        return response
    
class LogoutView(APIView):
    
    def post(self, request):
        logout(request)
        response=Response()
        response.delete_cookie("jwtoken")
        response.data={"message":"logedout..."}
        return response
    
class PostView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            profie=Profile.objects.get(user=request.user)
            serializer.save(author=profie)
            return Response({"message":"Post created", "data":serializer.data})
        return Response({"message":"Something went wrong", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
