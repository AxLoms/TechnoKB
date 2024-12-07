# Generated by Django 4.2.1 on 2024-12-06 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_total_count_alter_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stok',
            field=models.PositiveBigIntegerField(default=0, verbose_name='В наличии'),
        ),
        migrations.AddField(
            model_name='product',
            name='out_of_stok',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Не в наличии'),
        ),
    ]
