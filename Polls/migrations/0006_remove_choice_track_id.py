# Generated by Django 2.2.3 on 2019-07-31 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0005_choice_track_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='track_id',
        ),
    ]
