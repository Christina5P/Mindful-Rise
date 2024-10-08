# Generated by Django 4.2.9 on 2024-08-28 06:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvh69l0yv/image/upload/v1723788416/static/images/favicon.466a1a490666.png', max_length=255, verbose_name='image'),
        ),
    ]
