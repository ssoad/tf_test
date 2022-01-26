# Generated by Django 3.2.7 on 2022-01-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessSecurity', '0034_alter_quotationagreement_agreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='paypal_email',
        ),
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='paypal_id',
        ),
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='paypal_user_name',
        ),
        migrations.RemoveField(
            model_name='subscriptionorder',
            name='update_time',
        ),
        migrations.AddField(
            model_name='subscriptionorder',
            name='paypal_order_id',
            field=models.CharField(default='tete', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptionorder',
            name='paypal_subscription_id',
            field=models.CharField(default='asas', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriptionorder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]