from django.db import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your models here.


class Review(models.Model):
    book = models.ForeignKey('books.Book', related_name='reviews', on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.text


#@login_required
#def review_approve(request, pk):
#    review = get_object_or_404(Review, pk=pk)
#    review.approve()
#    return redirect('book_detail', pk=review.book.pk)


#@login_required
#def review_remove(request, pk):
#    review = get_object_or_404(Review, pk=pk)
#    review.delete()
#    return redirect('book_detail', pk=review.book.pk)