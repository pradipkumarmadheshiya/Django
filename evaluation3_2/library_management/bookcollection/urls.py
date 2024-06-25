from django.urls import path
from . import views

urlpatterns=[
    path("books/", views.bookList, name="bookList"),
    path("authors/", views.authorList, name="authorList"),
    path("authors/<int:id>/", views.bookDetail, name="bookDetail"),
    path("books/<int:id>/", views.authorDetail, name="authorDetail")
]