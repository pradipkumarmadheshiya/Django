from django.urls import  path
from . import views

urlpatterns = [
    path("", views.movieList, name="movieList"),
    path("heroes/", views.heroDetail, name="heroDetail"),
    path("heroes/<int:id>/", views.movieDetail, name="movieDetail")
]