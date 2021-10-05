# Generated by Django 3.2.7 on 2021-10-04 11:18

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_remove_post_reading_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Post Content'),
        ),
    ]