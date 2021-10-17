from django.contrib import admin
from Academy import models

# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.Content)
