from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(ListView):
    template_name = 'list.html'
    model = Book


class BookDetail(DetailView):
    template_name = 'detail.html'
    model = Book

class BookListAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
