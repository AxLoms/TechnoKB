# Generated by Django 4.2.1 on 2025-01-15 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_rename_images_productphoto_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]
