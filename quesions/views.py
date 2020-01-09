from django.shortcuts import render
from .models import Quesion, Tag
from django.shortcuts import get_object_or_404


def get_quessions_list(request, tags_slug=None):
    tag = None
    quession_list = Quesion.objects.all()
    if tags_slug:
        tag = get_object_or_404(Tag, slug=tags_slug)
        quession_list = quession_list.filter(tags=tag)
    return render(request, 'quessions/forum.html', {'qq': quession_list})
