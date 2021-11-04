# Generated by Django 3.2.7 on 2021-11-04 06:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0010_alter_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('bcs', 'BCS'), ('pcs', 'PCS')], max_length=255)),
                ('ticket_category', models.CharField(max_length=255, verbose_name='Category')),
                ('ticket_title', models.CharField(max_length=255, verbose_name='Title')),
                ('ticket_description', tinymce.models.HTMLField(verbose_name='Description')),
                ('ticket_attachment', models.ImageField(upload_to='ticket/', verbose_name='Attachment')),
                ('ticket_status', models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], max_length=255)),
                ('ticket_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
