import base64

import requests

from BusinessSecurity import models
from django.conf import settings

from django.core.mail import send_mail
from django.utils import timezone


def PaypalSubscriptionCheck():
    username = settings.PAYPAL_USER
    password = settings.PAYPAL_PASS
    busername = str(base64.b64encode(bytes(username, 'utf-8')))[1:].replace("'", "").replace("=", '')
    bpassword = str(base64.b64encode(bytes(password, 'utf-8')))[1:].replace("'", "")
    bearer = f"Basic {busername}6{bpassword}"

    all_subscriptions = models.SubscriptionOrder.objects.filter(is_active=True)
    for subscription in all_subscriptions:
        subscription_id = subscription.paypal_subscription_id

        url = f'{settings.PAYPAL_URL}billing/subscriptions/{subscription_id}/'

        headers = {
            'Content-type': 'application/json',
            'Authorization': bearer
        }
        r = requests.get(url, headers=headers)
        if r.json()['status'] != 'ACTIVE':
            subscription.is_active = False
            subscription.save()

    # url =
    # send_mail(
    #     'Subject here',
    #     f'Here is the message. Sent exactly at {timezone.now()}',
    #     'zulkar.techforing@gmail.com',
    #     ['hridoy.techforing@gmail.com'],
    #     fail_silently=False,
    # )
