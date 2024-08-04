from django.shortcuts import render
from django.urls import reverse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .serializers import UserSerializer,PostSerializer,ProfileSerializer
from .models import Profile, Post

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

import jwt,datetime

class JWTAuthmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [
            reverse('loginname'),
            reverse('registername'),
            reverse('resetpassword'),
            reverse('password_reset_confirm'),
            '/favicon.ico',
         ]        
    def __call__(self, request):
        # print("before if",request.path)
        # Check if the request path starts with any of the excluded paths
        if any(request.path.startswith(path) for path in self.excluded_paths) or request.path.startswith("/admin/"):
            # print("During if", request.path)
            return self.get_response(request)
        
        print("after if",request.path)
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token,'cap1.4b',algorithms=['HS256'])
        profile = Profile.objects.filter(user=payload['id']).first()
    
        if profile.user_type != 'author':
          return Response({'message':"Unauthorised"}, status=status.HTTP_401_UNAUTHORIZED)
        
        request.author = profile
        print("from mw", request.author)
       
        return  self.get_response(request)