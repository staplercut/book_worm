from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Book title', required=True)

    class Meta:
        model = Book
        fields = ('title', 'author_input', 'description', 'year_issued', 'publication_no', 'isbn', 'tags', 'book_cover')

    author_input = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
