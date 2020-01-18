from django.contrib import admin
from .models import Book
from django.utils.safestring import mark_safe


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'author', 'get_image', 'year', 'href'
    ]
    list_filter = [
        'title', 'author', 'year'
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" ')

    get_image.short_description = 'обложка'
