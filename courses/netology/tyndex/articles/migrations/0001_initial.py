# Generated by Django 2.2.10 on 2020-08-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Кликбейтный заголовок')),
                ('text', models.TextField(max_length=1500, verbose_name='Содержание статьи')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('products', models.ManyToManyField(blank=True, to='shop.Product', verbose_name='Связанные товары')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]