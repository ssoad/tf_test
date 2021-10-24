from django.contrib import admin
from BusinessSecurity import models

# Register your models here.


admin.site.register(models.NewsSubscriber)
admin.site.register(models.ServiceCategory)
admin.site.register(models.Service)
admin.site.register(models.SubService)
admin.site.register(models.InputFields)
admin.site.register(models.SubServiceInput)
admin.site.register(models.SubscriptionBasedPackage)
admin.site.register(models.SubscriptionFeatures)
admin.site.register(models.UserAllowed)
admin.site.register(models.Business)
admin.site.register(models.UsersBusiness)
admin.site.register(models.Events)
admin.site.register(models.RegisteredEvents)
