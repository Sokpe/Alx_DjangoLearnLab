from django.shortcuts import render
from .models import Book
from .forms import BookForm, ExampleForm
from django.contrib.auth.decorators import permission_required

# Example view using ExampleForm
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Process the form data
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})

# Other views...
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
