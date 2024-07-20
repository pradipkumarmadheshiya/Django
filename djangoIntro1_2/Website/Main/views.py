from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    context={"message":"Welcome to the website....."}
    return render(request, "Main/home.html", context)