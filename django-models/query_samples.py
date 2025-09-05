# relationship_app/query_samples.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage:
if __name__ == "__main__":
    # Create sample data
    author = Author.objects.create(name="John Doe")
    book1 = Book.objects.create(title="Book 1", author=author)
    book2 = Book.objects.create(title="Book 2", author=author)

    library = Library.objects.create(name="Main Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="Jane Doe", library=library)

    # Query all books by a specific author
    books_by_author = query_all_books_by_author("John Doe")
    print("Books by John Doe:")
    for book in books_by_author:
        print(book.title)

    # List all books in a library
    books_in_library = list_all_books_in_library("Main Library")
    print("\nBooks in Main Library:")
    for book in books_in_library:
        print(book.title)

    # Retrieve the librarian for a library
    librarian_for_library = retrieve_librarian_for_library("Main Library")
    print("\nLibrarian for Main Library:")
    print(librarian_for_library.name)