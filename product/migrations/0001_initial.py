# Generated by Django 4.2.1 on 2025-02-20 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество на текущий момент')),
                ('total_count', models.PositiveBigIntegerField(default=0, verbose_name='Общая количество')),
                ('average_price', models.FloatField(default=0, verbose_name='Средняя цена')),
                ('in_stock', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='В наличии')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('amount_of_transaction', models.PositiveSmallIntegerField(default=0, verbose_name='Количество транзакций')),
                ('is_published', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', max_length=3, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Приход', 'Приход'), ('Уход', 'Уход')], max_length=10, verbose_name='Действие')),
                ('count', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Фотография')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
        ),
    ]
