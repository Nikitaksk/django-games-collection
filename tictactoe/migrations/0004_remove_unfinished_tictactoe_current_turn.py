# Generated by Django 5.0.7 on 2024-07-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_unfinished_tictactoe_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unfinished_tictactoe',
            name='current_turn',
        ),
    ]
