from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Review, Author, Book
from .forms import BookForm, AuthorForm


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.published_date = timezone.now()
            item.save()
            return redirect('book_detail')
    else:
        form = BookForm()
    return render(request, 'books/book_edit.html', {'form': form})


def book_detail(request, pk):
    item = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'item': item})


def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.published_date = timezone.now()
            item.save()
            return redirect('book_detail')
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

