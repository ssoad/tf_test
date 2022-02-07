# Generated by Django 3.2.7 on 2022-02-04 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0050_subscriptionteam_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfield',
            name='subscriptionservice',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptionservice_service', to='BusinessSecurity.subscriptionservices'),
        ),
    ]