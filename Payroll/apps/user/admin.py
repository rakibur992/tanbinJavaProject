from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password')
    #     }),
    #     ('Personal info', {
    #         'fields': ('first_name', 'email', 'phone', 'age')
    #     }),
    #     ('Permissions', {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
    #                    'user_permissions'),
    #     }),
    #     ('Important dates', {
    #         'fields': ('last_login', 'date_joined')
    #     }),
    # )
    list_display = ('username', 'first_name', 'phone', 'is_staff')
    search_fields = ('username', 'first_name', 'email', 'phone')


admin.site.register(User, UserAdmin)
