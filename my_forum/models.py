from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


STATUS = (
    (1, 'опубликован'),
    (0, 'черновик'),
)


class Theme(models.Model):
    name = models.CharField(max_length=50, db_index=True,
                            verbose_name='название')
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тема'
        verbose_name_plural = 'темы'

    def get_absolute_url(self):
        return reverse('list_by_theme', args=[self.slug])


class ForumPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='post_author',
                               verbose_name='автор')
    theme = models.ForeignKey(Theme, null=True, on_delete=models.PROTECT,
                              verbose_name='тема')
    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.SlugField(max_length=50)
    content = models.TextField(verbose_name='контент')
    created = models.DateTimeField(auto_now=True, verbose_name='создан')
    update = models.DateTimeField(auto_now_add=True, verbose_name='изменен')
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='image', blank=True,
                              null=True, verbose_name='картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-created']
