# Generated by Django 4.2.8 on 2024-01-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0005_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
