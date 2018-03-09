from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=30)
    tags = models.TextField(default="")
    published_date = models.DateTimeField(blank=True, null=True)
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


