from django.db import models
from tinymce.models import HTMLField
from Account.models import User


# Create your models here.

class NewsSubscriber(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=264, verbose_name='Category Name')
    category_description = models.TextField(max_length=1000, verbose_name='Category Description')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Service Categories'


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='service_category')
    service_icon = models.ImageField(upload_to='service_icon/', verbose_name='Service Icon')
    service_title = models.CharField(max_length=264, verbose_name='Service Title')
    short_description = models.TextField(max_length=1000, verbose_name='Short Description')
    service_header = HTMLField(verbose_name='Service Header')
    service_body = HTMLField(verbose_name='Service Body')
    service_footer = HTMLField(verbose_name='Service Footer')
    has_sub_service = models.BooleanField(default=False, verbose_name='Has Sub Services')
    is_subscription_based = models.BooleanField(default=False, verbose_name='Is Subscription Based')
    total_customer = models.IntegerField(verbose_name='Total Customer')

    def __str__(self):
        return self.service_title

    class Meta:
        verbose_name_plural = 'Services'


class SubService(models.Model):
    sub_service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservice_service')
    title = models.CharField(max_length=264, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    total_customer = models.IntegerField(verbose_name='Total Customer')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Services'


class SubscriptionBasedPackage(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=264, verbose_name='Package Name')
    servers = models.IntegerField()
    websites = models.IntegerField()
    workstations = models.IntegerField()
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.package_name

    class Meta:
        verbose_name_plural = 'Subscription Based Packages'


class SubscriptionFeatures(models.Model):
    package = models.ForeignKey(SubscriptionBasedPackage, on_delete=models.CASCADE, related_name='feature_subscription')
    feature_name = models.CharField(max_length=264, verbose_name='Feature Name')

    def __str__(self):
        return self.feature_name

    class Meta:
        verbose_name_plural = 'Package Features'


class UserAllowed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allowed_user')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='allowed_service')

    def __str__(self):
        return f"{self.user.first_name} - {self.service.service_title}"

    class Meta:
        verbose_name_plural = 'Users Allowed'
