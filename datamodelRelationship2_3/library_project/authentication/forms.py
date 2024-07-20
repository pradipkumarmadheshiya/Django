from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "password1", "password2"]

class CreatePost(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title", "description"]

class CreateComment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["description"]