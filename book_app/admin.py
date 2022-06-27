from django.contrib import admin
from .models import Book, Writer


admin.site.register(Writer)


class RatingFilter(admin.SimpleListFilter):

    title = 'Сортировка по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'низкий'),
            ('от 40 до 59', 'средний'),
            ('от 60 до 100', 'высокий'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=59)
        if self.value() == 'от 60 до 100':
            return queryset.filter(rating__gte=60).filter(rating__lte=100)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'rating', 'choice', 'author', 'rating_status']
    list_editable = ['rating', 'choice']
    ordering = ['rating']
    list_per_page = 6
    search_fields = ['title']
    list_filter = [RatingFilter]

    @admin.display(description='Статус', ordering='rating')
    def rating_status(self, book: Book):
        if book.rating < 50:
            return 'Зачем такое читать?!'
        if book.rating < 70:
            return "На разок"
        return 'То что надо'
