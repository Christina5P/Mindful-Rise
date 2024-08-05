# Generated by Django 3.2.25 on 2024-08-04 19:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_images',
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvh69l0yv/image/upload/v1234567890/your_placeholder_image.jpg', max_length=255, verbose_name='image'),
        ),
    ]
