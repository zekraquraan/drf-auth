from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomerUserAdmin(UserAdmin):
    add_fieldsets = (
        ('None', {'fields': ('username', 'email', 'password1', 'password2')}),
        ('personal information', {'fields': ('first_name', 'last_name', 'phone_number')}),
    )


admin.site.register(CustomUser, CustomerUserAdmin)
