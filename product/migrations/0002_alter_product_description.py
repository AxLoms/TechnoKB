# Generated by Django 5.1.7 on 2025-03-24 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
    ]
