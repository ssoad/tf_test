# Generated by Django 3.2.7 on 2021-12-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsubscription',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
