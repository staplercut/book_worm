from django.shortcuts import render
from books.models import Book, Author

# Create your views here.


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'index/index.html', {'books': books}, {'authors': authors})




