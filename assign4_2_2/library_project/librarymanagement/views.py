from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm

class BookList(ListView):
    model=Book
    template_name="librarymanagement/bookList.html"
    context_object_name="books"

class BookDetail(DetailView):
    model=Book
    template_name="librarymanagement/bookDetail.html"

class BookCreate(CreateView):
    model=Book
    template_name="librarymanagement/bookCreate.html"
    form_class=BookForm
    # fields=["title", "author", "published_date", "ISBN", "pages", "cover"]
    success_url=reverse_lazy("BookList")

class BookUpdate(UpdateView):
    model=Book
    template_name="librarymanagement/bookUpdate.html"
    form_class=BookForm
    # fields=["title", "author", "published_date", "ISBN", "pages", "cover"]
    success_url=reverse_lazy("BookList")

class BookDelete(DeleteView):
    model=Book
    template_name="librarymanagement/bookDelete.html"
    success_url="/books/"