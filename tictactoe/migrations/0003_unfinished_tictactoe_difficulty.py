# Generated by Django 5.0.7 on 2024-07-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0002_tictactoe_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='unfinished_tictactoe',
            name='difficulty',
            field=models.CharField(default='easy', max_length=10),
        ),
    ]
