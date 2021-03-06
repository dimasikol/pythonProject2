# Generated by Django 4.0.1 on 2022-03-20 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('c_apps_kinopoisk', '0004_actor_surname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Актер', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанры', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-country'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='movieshots',
            options={'verbose_name': 'Фрагмент', 'verbose_name_plural': 'Фрагменты'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинг'},
        ),
        migrations.AlterModelOptions(
            name='rattingstar',
            options={'verbose_name': 'Рейтинг звезд', 'verbose_name_plural': 'Рейтинг звезд'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
