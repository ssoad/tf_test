# Generated by Django 3.2.7 on 2021-10-17 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academy', '0003_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text_instruction',
            field=models.FileField(upload_to='course/<django.db.models.fields.related.ForeignKey>/'),
        ),
    ]
