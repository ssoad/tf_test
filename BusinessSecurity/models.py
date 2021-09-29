from django.db import models


# Create your models here.

class NewsSubscriber(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
