from .models import User, Service
from django.views.generic import ListView, CreateView
from django.http import HttpResponse

class UserList(ListView):
    model=User
    template_name="paymentsection/userList.html"
    context_object_name="users"

class ServiceList(ListView):
    model=Service
    template_name="paymentsection/serviceList.html"
    context_object_name="services"

class UserCreate(CreateView):
    model=User
    template_name="paymentsection/userCreate.html"
    fields=["name", "email", "age", "gender"]
    success_url="/user/"

class ServiceCreate(CreateView):
    model=Service
    template_name="paymentsection/serviceCreate.html"
    fields=["type", "modeOfPayment", "company"]
    success_url="/service/"