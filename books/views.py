from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Author, Book
from .forms import BookForm
from django.http import HttpResponse
import string


def book_add(request, book, form):
    book.published_date = timezone.now()
    authors = form.cleaned_data['author_input']
    authors_list = list(filter(None, (' '.join(x.split()) for x in authors.split(','))))
    book.save()
    for x in authors_list:
        x = ' '.join(y.capitalize() for y in x.split())
        if Author.objects.filter(name=x).exists() and not book.authors.filter(name=x).exists():
            author = Author.objects.get(name=x)
            book.authors.add(author)
        elif not Author.objects.filter(name=x).exists():
            author = Author(name=x)
            author.save()
            book.authors.add(author)
    return redirect('books:book_detail', pk=book.pk)


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)

            t = form.cleaned_data['title']
            book.title = ' '.join(
                w.capitalize() for w in t.translate(str.maketrans('', '', string.punctuation)).split())
            book.post_author = request.user
            if Book.objects.filter(title=book.title).exists():
                return HttpResponse('Book title already exists')
            else:
                return book_add(request, book, form)
    else:
        form = BookForm()
        return render(request, 'books/book_edit.html', {'form': form})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = ", ".join(getattr(author, 'name') for author in book.authors.all())
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            return book_add(request, book, form)
    else:
        form = BookForm(instance=book, initial={'author_input': authors})
        return render(request, 'books/book_edit.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('index:index')




