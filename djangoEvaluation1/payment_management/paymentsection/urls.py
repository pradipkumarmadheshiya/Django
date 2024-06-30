from django.urls import path
from .views import UserList, ServiceList, UserCreate, ServiceCreate

urlpatterns=[
    path("user/", UserList.as_view(), name="userList"),
    path("service/", ServiceList.as_view(), name="serviceList"),
    path("createUser/", UserCreate.as_view(), name="userCreate"),
    path("createService/", ServiceCreate.as_view(), name="serviceCreate")
]