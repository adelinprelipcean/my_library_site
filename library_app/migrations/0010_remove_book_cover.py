# Generated by Django 4.2.8 on 2024-01-03 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0009_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
    ]
