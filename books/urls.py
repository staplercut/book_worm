from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^new/$', views.book_new, name='book_new'),
    url(r'^(?P<pk>\d+)/edit/', views.book_edit, name='book_edit'),
    url(r'^author/(?P<pk>\d+)/$', views.author_detail, name='author_detail'),
    url(r'^author/new/$', views.author_new, name='author_new'),
    url(r'^author/(?P<pk>\d+)/edit/', views.author_edit, name='author_edit'),
    url(r'^(?P<pk>\d+)/delete', views.book_delete, name='book_delete'),
    url(r'^author/(?P<pk>\d+)/delete', views.author_delete, name='author_delete')
]