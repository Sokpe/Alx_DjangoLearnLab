# create.md
## Create Operation
**Command:**
python
from bookshelf.models import Book
book = Book(title='1984', author='George Orwell', publication_year=1949)
book.save()


*Output:*
*The book instance will be saved to the database with id.*
