from django.contrib import admin
from Account.models import User, Permissions
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AdminUser(UserAdmin):
    ordering = ('-date_joined',)
    search_fields = ('email', 'first_name', 'last_name', 'phone_number',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'gender', 'is_bcs',)
    list_display = ('email', 'first_name', 'country', 'gender', 'date_joined', 'is_bcs', 'is_active')
    fieldsets = (
        ('Login Info', {'fields': ('email', 'password')}),
        ('User Information',
         {'fields': ('first_name', 'last_name', 'gender', 'profile_pic', 'birth_date', 'country', 'phone_number',)}),
        ('Permissions', {'fields': ('is_bcs', 'is_active', 'is_staff', 'is_superuser', 'newsletter',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )


admin.site.register(User, AdminUser)
admin.site.register(Permissions)
