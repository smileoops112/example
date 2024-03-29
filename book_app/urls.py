from .views import get_info_about_book, get_info_about_one_book
from django.urls import path

urlpatterns = [
    path('', get_info_about_book),
    path('book/<slug:slug_book>', get_info_about_one_book, name='book-info')
]