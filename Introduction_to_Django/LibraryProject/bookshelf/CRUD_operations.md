# CRUD Operations

## Create Operation
### Command
python
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()


*Output*
The book instance will be saved to the database with id.

*Retrieve Operation*
*Command*

book = Book.objects.get(title='1984')
print(book.title, book.author, book.publication_year)


*Output*

1984 George Orwell 1949


*Update Operation*
*Command*

book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
print(book.title)


*Output*

Nineteen Eighty-Four


*Delete Operation*
*Command*

book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
print(Book.objects.all())


*Output*

<QuerySet []>


*models.py*

bookshelf/models.pyfrom django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


*Steps to Perform CRUD Operations*
1. Open Django shell: `python manage.py shell`
2. Import the Book model: `from bookshelf.models import Book`
3. Perform CRUD operations as documented above.

*Expected Output*
The expected output for each operation is documented above. The CRUD operations will create, retrieve, update, and delete a book instance in the database.
