from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', BooksModelView.as_view(), name="index"),
    path('book/', BookListView.as_view(), name="book_list"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('publisher/', PublisherListView.as_view(), name="publisher_list"),
    path('publisher/<int:pk>/', PublisherDetailView.as_view(), name="publisher_detail"),
    path('author/', AuthorListView.as_view(), name="author_list"),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name="author_detail"),
]
