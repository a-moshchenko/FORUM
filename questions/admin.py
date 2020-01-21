from django.contrib import admin
from .models import Question
from .models import GetTagListMixin


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin, GetTagListMixin):
    list_display = [
        'id', 'name', 'author', 'likes', 'views', 'tag_list',
        'time_since_publication'
    ]
