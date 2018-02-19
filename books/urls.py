from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^book/(?P<pk>\d+)/edit/', views.book_edit, name='book_edit'),
    url(r'^author/(?P<pk>\d+)/$', views.author_detail, name='author_detail'),
    url(r'^author/new/$', views.author_new, name='author_new'),
    url(r'^author/(?P<pk>\d+)/edit/', views.author_edit, name='author_edit'),
]