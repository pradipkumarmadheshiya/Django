from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path("publishers/", views.publisher, name="publisher"),
    path("publishers/<int:publisherId>/", views.bookDetails, name="bookDetails"),
]