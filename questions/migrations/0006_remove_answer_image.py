# Generated by Django 3.0.3 on 2020-03-12 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200312_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='image',
        ),
    ]