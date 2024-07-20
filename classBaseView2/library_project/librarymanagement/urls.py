from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns=[
    path("books/", BookList.as_view(), name="BookList"),
    path("books/<int:pk>/", BookDetail.as_view(), name="BookDetail"),
    path("create/", BookCreate.as_view(), name="BookCreate"),
    path("update/<int:pk>/", BookUpdate.as_view(), name="BookUpdate"),
    path("delete/<int:pk>/", BookDelete.as_view(), name="BookDelete")
]