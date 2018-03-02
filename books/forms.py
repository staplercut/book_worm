from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author_input', 'description', 'year_issued', 'publication_no', 'isbn', 'tags', 'book_cover')

    author_input = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}))

    def __init__(self,  *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['tags'].required = True
        self.fields['year_issued'].required = True
        self.fields['publication_no'].required = True
        self.fields['isbn'].required = True


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'tags')

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True


class ImageUploadForm(forms.Form):
    image = forms.ImageField()