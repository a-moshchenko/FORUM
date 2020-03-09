from django.contrib import admin
from .models import Question,  Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'author', 'likes', 'views',
        'time_since_publication'
    ]


admin.site.register(Answer)
