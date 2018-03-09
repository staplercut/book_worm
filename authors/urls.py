from django.conf.urls import url
from .views import (
    author_detail,
    author_new,
    author_edit,
    author_delete
)

app_name = 'authors'
urlpatterns = [
    url(r'^author/(?P<pk>\d+)/$', author_detail, name='author_detail'),
    url(r'^author/new/$', author_new, name='author_new'),
    url(r'^author/(?P<pk>\d+)/edit/', author_edit, name='author_edit'),
    url(r'^author/(?P<pk>\d+)/delete', author_delete, name='author_delete')
]