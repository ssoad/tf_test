from django.core.mail import send_mail
from django.utils import timezone


def PaypalSubscriptionCheck():
    print('Test')
    send_mail(
        'Subject here',
        f'Here is the message. Sent exactly at {timezone.now()}',
        'zulkar.techforing@gmail.com',
        ['hridoy.techforing@gmail.com'],
        fail_silently=False,
    )
