from django.urls import path
from . import views

urlpatterns=[
    path("tasks/", views.get_all_tasks, name="tasks"),
    path("edit/<int:pk>/", views.edit_delete_tasks, name="edit-delete")
]