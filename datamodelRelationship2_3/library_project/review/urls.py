from django.urls import path
from . import views

urlpatterns=[
    path("", views.ReviewView.as_view(), name="index"),
    path("thankYou/", views.ThankYouView.as_view(), name="thankYou"),
    path("all/", views.ReviewViewList.as_view(), name="viewList")
]