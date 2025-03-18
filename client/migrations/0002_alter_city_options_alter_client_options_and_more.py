# Generated by Django 4.2.1 on 2025-03-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='client',
            name='telephone',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Названия'),
        ),
    ]
