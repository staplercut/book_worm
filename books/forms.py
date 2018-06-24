from django import forms
from .models import Book, Author

import string


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Book title', required=True)

    class Meta:
        model = Book
        fields = ('title', 'author_input', 'description', 'year_issued', 'publication_no', 'isbn', 'tags', 'book_cover')

    # author_input = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))
    author_input = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    # this helps to trigger unique validation even if words in lowercase
    def clean_title(self):
        pre_title = self.cleaned_data['title']
        title = ' '.join(w.capitalize() for w in pre_title.translate(str.maketrans('', '', string.punctuation)).split())
        return title
