# Generated by Django 3.1.1 on 2020-09-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Список категорий',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Имя параметра',
                'verbose_name_plural': 'Список имен параметров',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название')),
                ('model', models.CharField(blank=True, max_length=80, verbose_name='Модель')),
                ('external_id', models.PositiveIntegerField(verbose_name='Внешний ИД')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('price_rrc', models.PositiveIntegerField(verbose_name='Рекомендуемая розничная цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Список продуктов',
                'ordering': ('category', '-name'),
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Список параметров',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на файл прайса')),
                ('state', models.BooleanField(default=True, verbose_name='Cтатус получения заказов')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Список магазинов',
                'ordering': ('-name',),
            },
        ),
    ]
