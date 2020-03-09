from rest_framework import serializers

from .models import ForumPost


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ('image', 'theme', 'content', 'title')
