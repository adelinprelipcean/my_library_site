# Generated by Django 4.2.8 on 2024-01-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_remove_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
