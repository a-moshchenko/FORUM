from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('forum_for_tag', args=[self.slug])


class Quesion(models.Model):
    name = models.CharField(max_length=100, verbose_name='вопрос')
    body = models.TextField(verbose_name='описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='автор')
    likes = models.IntegerField(default=0, verbose_name='лайки')
    views = models.IntegerField(default=0, verbose_name='просмотры')
    created = models.DateTimeField(auto_now=True, verbose_name='создан')
    tags = models.ManyToManyField(Tag,)

    def __str__(self):
        return self.name

    def tags_list(self):
        return [i for i in self.tags.all()]

    class Meta:
        ordering = ['-created']
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
