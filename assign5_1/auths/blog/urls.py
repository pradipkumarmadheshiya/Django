from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.home, name="home"),
    path("createUser/", views.create_user, name="createUser"),
    path("loginUser/", views.login_user, name="loginUser"),
    path("logoutUser/", views.logout_user, name="logoutUser"),
    path("user/", views.user_profile, name="user"),
    path("createPost/", views.create_post, name="createPost"),
    path("postList/", views.post_list, name="postList"),
    path("editPost/<int:id>/", views.edit_post, name="editPost"),
    path("postDetail/<int:id>/", views.post_detail, name="postDetail"),
    path("postDelete/<int:id>/", views.post_delete, name="postDelete"),
    path("createComment/<int:id>/", views.create_comment, name="createComment")
]