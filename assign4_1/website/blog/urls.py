from django.urls import path
from .views import PostList, CommentList, PostCreate, PostUpdate, PostDelete

urlpatterns=[
    path("list/", PostList.as_view(), name="PostList"),
    path("list/<int:pk>/", CommentList.as_view(), name="CommentDetail"),
    path("create/", PostCreate.as_view(), name="PostCreate"),
    path("update/<int:pk>/", PostUpdate.as_view(), name="PostUpdate"),
    path("delete/<int:pk>/", PostDelete.as_view(), name="PostDelete")
]