from django.contrib import admin
from .models import Question,  Answer, Tags


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'author', 'likes', 'views',
        'time_since_publication'
    ]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Answer)
