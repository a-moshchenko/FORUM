from django.db import models






class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    author = models.CharField(max_length=50, verbose_name='автор')
    description = models.TextField(verbose_name='описание')
    year = models.SmallIntegerField(verbose_name='год')
    href = models.URLField(verbose_name='ссылка')
    image = models.ImageField(upload_to='book_img', verbose_name='обложка',
                              default=None)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
