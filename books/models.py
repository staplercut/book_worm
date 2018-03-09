from django.db import models
from authors.models import Author
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    year_issued = models.SmallIntegerField()
    authors = models.ManyToManyField(Author, blank=True)
    tags = models.TextField(default="")
    publication_no = models.SmallIntegerField(default='1')
    isbn = models.SmallIntegerField()
    book_cover = models.ImageField(upload_to='pics/', default='pics/None/no_cover.png')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def save(self, **kwargs):
        self.published_date = timezone.now()
        super(Book, self).save(**kwargs)

    def approved_reviews(self):
        return self.reviews.filter(approved_review=True)

    def __str__(self):
        return self.title
