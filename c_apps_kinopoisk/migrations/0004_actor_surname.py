# Generated by Django 4.0.1 on 2022-02-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_apps_kinopoisk', '0003_alter_actor_description_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='surname',
            field=models.CharField(default=0, max_length=100, verbose_name='фамилия'),
            preserve_default=False,
        ),
    ]