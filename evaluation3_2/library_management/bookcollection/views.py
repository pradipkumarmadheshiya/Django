from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from . import models

def bookList(request):
    books=models.Book.objects.all()
    return render(request, "bookcollection/bookList.html", {"books":books})

def authorList(request):
    authors=models.Author.objects.all()
    return render(request, "bookcollection/authorList.html", {"authors":authors})

def bookDetail(request, id):
    author=get_object_or_404(models.Author, id=id)
    authorBooks=author.book.all()
    return render(request, "bookcollection/bookDetail.html", {"authorBooks":authorBooks, "authorName":author})

def authorDetail(request, id):
    book=get_object_or_404(models.Book, id=id)
    bookAuthors=book.authors.all()
    return render(request, "bookcollection/authorDetail.html", {"authors":bookAuthors, "bookName":book})