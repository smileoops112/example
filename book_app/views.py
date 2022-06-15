from django.shortcuts import render, get_object_or_404
from .models import Book


def get_info_about_book(request):
    books = Book.objects.all()
    return render(request, 'book_app/books_info.html', context={'books': books})


def get_info_about_one_book(request, book_info):

    book = get_object_or_404(Book, pk=book_info)
    return render(request, 'book_app/one_book_info.html', context={'book': book})
