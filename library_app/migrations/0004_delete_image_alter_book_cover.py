# Generated by Django 4.2.8 on 2024-01-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='../media'),
        ),
    ]
