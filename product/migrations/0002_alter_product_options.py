# Generated by Django 5.1.7 on 2025-03-18 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
