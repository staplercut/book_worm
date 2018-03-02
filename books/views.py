from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Review, Author, Book
from .forms import BookForm, AuthorForm, ImageUploadForm
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
import string


def book_add(request, book, form):
    book.published_date = timezone.now()

    #book.book_cover = request.FILES['book_cover']

    authors = form.cleaned_data['author_input']
    authors_list = list(filter(None, (' '.join(x.split()) for x in authors.split(','))))
    print(authors_list)
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
    print(authors)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            #print(request.FILES.keys())
            print(book.book_cover)
            return book_add(request, book, form)
    else:
        form = BookForm(instance=book, initial={'author_input': authors})
        return render(request, 'books/book_edit.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.published_date = timezone.now()
            x = form.cleaned_data['name']
            author.name = ' '.join(y.capitalize() for y in x.split())
            author.post_author = request.user
            if Author.objects.filter(name=author.name).exists():
                return HttpResponse('Author already exists')
            else:
                author.save()
                return redirect('books:author_detail', pk=author.pk)
    else:
        form = AuthorForm()
        return render(request, 'books/author_edit.html', {'form': form})


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.published_date = timezone.now()
            author.post_author = request.user
            author.save()
            return redirect('books:author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
        return render(request, 'books/author_edit.html', {'form': form})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'author': author})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('index:index')


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('index:index')


def upload_pic(request, pk):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Book.objects.get(pk=pk)
            m.book_cover = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')









@login_required
def review_approve(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.approve()
    return redirect('book_detail', pk=review.book.pk)

@login_required
def review_remove(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('book_detail', pk=review.book.pk)

