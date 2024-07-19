from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "password"]
        extra_kwargs={"password":{"write_only":True}}

        def create(self, validated_data):
            user=User.objects.create_user(**validated_data)
            return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["id", "user", "user_type"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"