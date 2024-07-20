from django.http import HttpResponse
from django.shortcuts import render
from . import models

def books(request):

    showBooks=models.Book.objects.all()

    return render(request, "bookssection/booksList.html", {"books":showBooks})

def publisher(request):

    showPublisher=models.Publisher.objects.all()

    return render(request, "bookssection/publisherDetail.html", {"publishers":showPublisher})

def bookDetails(request, publisherId):
    publisherDetails=models.Publisher.objects.get(pk=publisherId)
    publisherBook=models.Book.objects.filter(publisher=publisherId)
    return render(request, "bookssection/bookDetails.html", {"publisherName":publisherDetails, "bookName":publisherBook})