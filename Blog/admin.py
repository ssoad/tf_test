from django.contrib import admin
from Blog import models


# Register your models here.
admin.site.register(models.BlogCategory)
admin.site.register(models.BlogSubCategory)
admin.site.register(models.Post)
admin.site.register(models.Comment)
