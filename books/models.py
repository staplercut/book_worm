from django.db import models
from django.utils import timezone
from django.conf import settings


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Review(models.Model):
    book = models.ForeignKey('books.Book', related_name='reviews', on_delete=models.PROTECT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    year_issued = models.SmallIntegerField()
    authors = models.ManyToManyField(Author)
    publication_no = models.SmallIntegerField()
    isbn = models.SmallIntegerField()
    book_cover = models.ImageField(upload_to='pics/', default='pics/None/no_cover.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_reviews(self):
        return self.reviews.filter(approved_review=True)

    def __str__(self):
        return self.title





