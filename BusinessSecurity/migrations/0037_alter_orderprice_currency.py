# Generated by Django 3.2.7 on 2022-01-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0036_subscriptionorder_category_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderprice',
            name='currency',
            field=models.CharField(choices=[('euro', 'EURO €'), ('pound', 'POUND £'), ('usd', 'USD $')], max_length=255),
        ),
    ]
