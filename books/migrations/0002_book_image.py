# Generated by Django 3.0.2 on 2020-01-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=None, upload_to='book_img', verbose_name='обложка'),
        ),
    ]
