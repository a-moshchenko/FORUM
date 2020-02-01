from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def get_absolut_url(self):
        return reverse('forum_for_tag', args=[self.name])

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=100, verbose_name='вопрос')
    body = models.TextField(verbose_name='описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='автор')
    likes = models.IntegerField(default=0, verbose_name='лайки')
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True,)
    tags = models.ManyToManyField(Tags, blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])

    def time_since_publication(self):
        time = (timezone.now() - self.created) // 60
        name = 'мин.'
        if time.seconds > 60:
            time = (timezone.now() - self.created) // 3600
            name = 'час.'
            if time.seconds > 24:
                time = (timezone.now() - self.created) // 86400
                name = 'дн.'
                if time.seconds > 30:
                    time = (timezone.now() - self.created) // 2628002
                    name = 'дн.'
                    if time.seconds > 12:
                        time = (timezone.now() - self.created) // 31536000
                        if (time.seconds % 100) == 11 or 12 or 13 or 14 or 15:
                            name = 'лет'
                        elif (time.seconds % 10) == 2 or 3 or 4:
                            name = 'года'
                        elif (time.seconds % 10) == 1:
                            name = 'год'
                        else:
                            name = 'лет'

        return f' {time.seconds} {name} '


class Answer(models.Model):
    author = models.CharField(max_length=60, verbose_name='автор')
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 verbose_name='вопрос')
    code = models.TextField(verbose_name='пример кода', blank=True)
    image = models.ImageField(upload_to='answer_img')
    create_on = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    update_on = models.DateTimeField(auto_now=True, verbose_name='обновлен')

    def __str__(self):
        return f' ответ {self.author}'
