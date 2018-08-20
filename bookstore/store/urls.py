from django.conf.urls import url
from .views import BookList, AddBookView, UpdateBookView

urlpatterns = [
    url(r'^$', BookList.as_view(), name='book_list'),
    url(r'^create/$', AddBookView.as_view(), name='book_create'),
    url(r'^update/(?P<id>[\d-]+)/$', UpdateBookView.as_view(), name='book_update'),
]
