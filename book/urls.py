from django.urls import path

from .views import BookList, BookDetail, BookListAPI

urlpatterns = [
    path("list/", BookList.as_view()),
    path("detail/<int:pk>", BookDetail.as_view()),
    path("api/", BookListAPI.as_view()),
]
