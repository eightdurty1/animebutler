# Generated by Django 4.0.4 on 2022-05-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_interest_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='genre',
            field=models.CharField(choices=[(1, 'Action'), (2, 'Adventure'), (4, 'Comedy'), (8, 'Drama'), (10, 'Fantasy'), (14, 'Horror'), (40, 'Psychological'), (22, 'Romance'), (24, 'Sci-Fi'), (25, 'Shoujo'), (27, 'Shounen'), (36, 'Slice of Life')], default='Action', max_length=20),
        ),
    ]
