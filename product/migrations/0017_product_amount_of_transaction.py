# Generated by Django 4.2.1 on 2025-01-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount_of_transaction',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Популярное'),
        ),
    ]
