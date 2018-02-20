from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Review, Author, Book
from .forms import BookForm, AuthorForm, ImageUploadForm
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def book_new(request):
    if request.method == "POST":
        author_list = []
        if 'post author' in request.POST:
            form = BookForm(request.POST)
            if form.is_valid():
                author = form.cleaned_data['author']
                author_list.extend(author)
        elif 'post book' in request.POST:
            form = BookForm(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.published_date = timezone.now()
                book.authors.add(*author_list)
                book.save()
                return redirect('book_detail')
    else:
        form = BookForm()
        return render(request, 'books/book_edit.html', {'form': form})


def upload_pic(request, pk):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Book.objects.get(pk=pk)
            m.book_cover = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')


def book_detail(request, pk):
    item = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'item': item})


def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.published_date = timezone.now()
            author.save()
            return redirect('author_detail')
    else:
        form = BookForm()
    return render(request, 'books/author_edit.html', {'form': form})


def author_detail(request, pk):
    item = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'item': item})






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

