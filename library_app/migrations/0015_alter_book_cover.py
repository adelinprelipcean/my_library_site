# Generated by Django 4.2.8 on 2024-01-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0014_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(null=True, upload_to='../media'),
        ),
    ]