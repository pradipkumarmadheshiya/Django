from django.urls import path

from . import views

urlpatterns=[
    path("blogList/", views.blogList, name="blogList"),
    path("blogList/<int:id>/", views.blogDetails, name="blogDetails"),
]