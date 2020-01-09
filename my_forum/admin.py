from django.contrib import admin
from .models import ForumPost, Theme


@admin.register(ForumPost)
class AdminForumPost(admin.ModelAdmin):
    list_display = [
        'title', 'theme', 'author', 'created', 'update', 'status'
    ]
    list_filter = [
        'theme', 'author', 'created', 'status'
    ]
    list_editable = [
        'status', 'theme'
    ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
