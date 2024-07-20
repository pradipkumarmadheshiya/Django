from django.urls import path
from . import views

urlpatterns=[
    path("home/", views.home, name="home"),
    path("signup/", views.create_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("user/", views.user_profile, name="user"),
    path("createPost/", views.create_post, name="createPost"),
    path("postList/", views.post_list, name="postList"),
    path("editPost/<int:id>/", views.edit_post, name="editPost"),
    path("createComment/<int:id>/", views.create_comment, name="createComment")
]