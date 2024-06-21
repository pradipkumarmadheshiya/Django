from django.shortcuts import render
from . import models

def books(request):

    showBooks=models.Book.objects.all()

    return render(request, "bookssection/booksList.html", {"books":showBooks})