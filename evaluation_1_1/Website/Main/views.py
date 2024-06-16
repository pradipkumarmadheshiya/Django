from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context={"message":"Welcome to the website....."}
    return render(request, "Main/home.html", context)