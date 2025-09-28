from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated", "IsAuthenticated"
class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

