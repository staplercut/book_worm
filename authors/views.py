from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from books.models import Author
from .forms import AuthorForm


def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.published_date = timezone.now()
            author.post_author = request.user
            author.save()

            # FIXME No need to make handle validation in view, it is a part of form clean method
            # x = form.cleaned_data['name']
            # author.name = ' '.join(y.capitalize() for y in x.split())

            # FIXME No need to make handle validation, it is a part of form validation by model attrs
            # if Author.objects.filter(name=author.name).exists():
            #     return HttpResponse('Author already exists')
            # else:
            return redirect('authors:author_detail', pk=author.pk)
        return render(request, 'authors/author_edit.html', {'form': form})
    else:
        form = AuthorForm()
        return render(request, 'authors/author_edit.html', {'form': form})


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.published_date = timezone.now()
            author.post_author = request.user
            author.save()
            return redirect('authors:author_detail', pk=author.pk)
        return render(request, 'authors/author_edit.html', {'form': form})
    else:
        form = AuthorForm(instance=author)
        return render(request, 'authors/author_edit.html', {'form': form})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('index:index')