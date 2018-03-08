from django.conf.urls import url
from .views import (
    book_detail,
    book_new,
    book_edit,
    author_detail,
    author_new,
    author_edit,
    book_delete,
    author_delete
)

app_name = 'books'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', book_detail, name='book_detail'),
    url(r'^new/$', book_new, name='book_new'),
    url(r'^(?P<pk>\d+)/edit/', book_edit, name='book_edit'),
    url(r'^author/(?P<pk>\d+)/$', author_detail, name='author_detail'),
    url(r'^author/new/$', author_new, name='author_new'),
    url(r'^author/(?P<pk>\d+)/edit/', author_edit, name='author_edit'),
    url(r'^(?P<pk>\d+)/delete', book_delete, name='book_delete'),
    url(r'^author/(?P<pk>\d+)/delete', author_delete, name='author_delete')
]