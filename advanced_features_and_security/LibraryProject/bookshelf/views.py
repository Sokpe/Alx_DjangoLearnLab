from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Using Django's ORM
    return render(request, 'bookshelf/book_list.html', {'books': books})

def search_books(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)  # Safe ORM query
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
