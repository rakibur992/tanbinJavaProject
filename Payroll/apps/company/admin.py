from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib import admin
from django.conf import settings
from .models import Company


admin.site.register(Company)
