# Generated by Django 3.2.25 on 2024-08-05 16:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20240804_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
