# Generated by Django 3.0.3 on 2020-02-22 18:47

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='вопрос')),
                ('body', models.TextField(verbose_name='описание')),
                ('author', models.CharField(max_length=50, verbose_name='автор')),
                ('likes', models.IntegerField(default=0, verbose_name='лайки')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='просмотры')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60, verbose_name='автор')),
                ('code', models.TextField(blank=True, verbose_name='пример кода')),
                ('image', models.ImageField(upload_to='answer_img')),
                ('create_on', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('update_on', models.DateTimeField(auto_now=True, verbose_name='обновлен')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question', verbose_name='вопрос')),
            ],
        ),
    ]