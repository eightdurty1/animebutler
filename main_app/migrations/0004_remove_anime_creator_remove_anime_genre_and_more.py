# Generated by Django 4.0.4 on 2022-05-04 18:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_watchlist_anime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='language',
        ),
        migrations.RemoveField(
            model_name='anime',
            name='producer',
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=10),
        ),
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.CharField(default='No url', max_length=200),
        ),
        migrations.AddField(
            model_name='anime',
            name='mal_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='anime',
            name='producers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=10),
        ),
        migrations.AddField(
            model_name='anime',
            name='status',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='anime',
            name='year',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
