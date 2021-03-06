# Generated by Django 3.0.3 on 2020-03-04 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_forum', '0002_auto_20200222_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='создан')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='изменен')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_forum.ForumPost', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
    ]
