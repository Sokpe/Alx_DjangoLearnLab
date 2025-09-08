from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data['title']
        # Example validation: Title must not be empty
        if not title.strip():
            raise forms.ValidationError("Title cannot be empty")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        # Example validation: Author must not be empty
        if not author.strip():
            raise forms.ValidationError("Author cannot be empty")
        return author
