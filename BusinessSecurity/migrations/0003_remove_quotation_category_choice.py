# Generated by Django 3.2.7 on 2022-01-01 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0002_quotation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='category_choice',
        ),
    ]
