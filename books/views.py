from .models import Book
from django.views.generic import ListView


class BookListView(ListView):
    template_name = 'book/home.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
