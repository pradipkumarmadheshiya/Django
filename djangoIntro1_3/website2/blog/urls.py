from django.urls import path
from . import views

urlpatterns=[
    path("blogList/", views.blogPage, name="blogPage"),
    path("blogList/<int:postId>/", views.blogDetails, name="blogDetails"),
]