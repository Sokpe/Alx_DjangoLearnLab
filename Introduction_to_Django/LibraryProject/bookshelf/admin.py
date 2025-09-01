from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for author and publication_year
    list_filter = ('author', 'publication_year')

    # Enable search by title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)