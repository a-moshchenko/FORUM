from django.shortcuts import render
from .models import Book


def get_book_list(request):
    books = Book.objects.all()
    return render(request, 'book/home.html', {'books': books})
