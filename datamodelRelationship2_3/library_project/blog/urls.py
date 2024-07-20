from django.urls import path
from .views import PostList, PostCreate, PostUpdate, PostDelete

urlpatterns=[
    path("list/", PostList.as_view(), name="PostList"),
    path("create/", PostCreate.as_view(), name="PostCreate"),
    path("update/<int:pk>/", PostUpdate.as_view(), name="PostUpdate"),
    path("delete/<int:pk>/", PostDelete.as_view(), name="PostDelete")
]