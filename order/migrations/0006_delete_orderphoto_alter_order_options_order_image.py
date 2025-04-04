# Generated by Django 5.1.7 on 2025-03-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderphoto_alter_order_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderPhoto',
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Фотография'),
        ),
    ]
