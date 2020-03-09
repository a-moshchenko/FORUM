from django.contrib import admin
from .models import ForumPost, Theme, PostComment
from django.utils.safestring import mark_safe


@admin.register(ForumPost)
class AdminForumPost(admin.ModelAdmin):
    list_display = [
        'title', 'theme', 'author', 'created', 'update', 'status', 'get_image'
    ]
    list_filter = [
        'theme', 'author', 'created', 'status'
    ]
    list_editable = [
        'status', 'theme'
    ]
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" ')

    get_image.short_description = 'изображения'


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(PostComment)
