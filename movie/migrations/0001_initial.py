# Generated by Django 4.2.2 on 2023-06-10 15:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=1, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=150, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movie/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2023, verbose_name='Год выхода')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('world_premiere', models.DateTimeField(default=datetime.date.today, verbose_name='Премьера в мире')),
                ('budget', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в мире')),
                ('url', models.SlugField(max_length=150, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movie.actor', verbose_name='Актеры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movie.actor', verbose_name='Режиссер')),
                ('genres', models.ManyToManyField(to='movie.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Значение',
                'verbose_name_plural': 'Значения',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('text', models.TextField(max_length=5000, verbose_name='Коментарий')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.review', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='ip')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ratingstar', verbose_name='star')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='movie_shots/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Кадр')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
    ]
