# Generated by Django 3.2.7 on 2021-10-04 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_rename_shot_description_post_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reading_time',
        ),
    ]