from django.shortcuts import render
from books.models import Book, Author

# Create your views here.


def index(request):
    books_all = Book.objects.all()
    authors_all = Author.objects.all()
    return render(request, 'index/index.html', {'authors_all': authors_all, 'books_all': books_all})




