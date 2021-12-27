from django.contrib import admin
from BusinessSecurity import models


# Register your models here.



admin.site.register(models.NewsSubscriber)
admin.site.register(models.ServiceCategory)
admin.site.register(models.Service)
admin.site.register(models.SubscriptionServices)
admin.site.register(models.ServiceAssigned)
admin.site.register(models.Tracking)
admin.site.register(models.SubService)

admin.site.register(models.InputFields)
admin.site.register(models.SelectChoice)
admin.site.register(models.SelectChoiceRelation)
admin.site.register(models.SubServiceInput)
admin.site.register(models.UserSubserviceInput)
admin.site.register(models.Order)
admin.site.register(models.SubscriptionOrder)
admin.site.register(models.OrderPrice)
admin.site.register(models.OrderStaff)

admin.site.register(models.SubscriptionBasedPackage)
admin.site.register(models.SubscriptionFeatures)
admin.site.register(models.UserAllowed)
admin.site.register(models.Business)
admin.site.register(models.UsersBusiness)
admin.site.register(models.Events)
admin.site.register(models.RegisteredEvents)

admin.site.register(models.Ticket)
admin.site.register(models.TicketStaff)
admin.site.register(models.TicketComment)

admin.site.register(models.Notification)
