from django.contrib.contenttypes.models import ContentType
from .models import Like
from questions.models import Question
from django.shortcuts import get_object_or_404, redirect


def create_like(request, id):
    obj = get_object_or_404(Question, id=id)
    user = request.user
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    response = redirect('forum')
    return response
