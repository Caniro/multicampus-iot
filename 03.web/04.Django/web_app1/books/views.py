from django.shortcuts import render
from django.views import generic
from books.models import *

class BooksModelView(generic.TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = [
            ('Book', 'books:book_list'),
            ('Author', 'books:author_list'),
            ('Publisher', 'books:publisher_list')
        ]
        return context

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

class BookDetailView(generic.DetailView):
    model = Book

class PublisherListView(generic.ListView):
    model = Publisher

class PublisherDetailView(generic.DetailView):
    model = Publisher

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
