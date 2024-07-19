from django.urls import path
from . import views

urlpatterns=[
    path("movies/", views.get_all_movies, name="movies"),
    path("edit/<int:pk>/", views.edit_delete_movies, name="edit_delete")
]