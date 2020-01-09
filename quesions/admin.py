from django.contrib import admin
from .models import Quesion, Tag


@admin.register(Quesion)
class QuesionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'author', 'likes', 'views', 'tags_list'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
