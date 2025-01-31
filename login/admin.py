from django.contrib import admin
from .models import UserLogin

# Register your models here.

# class AdminUser(admin.ModelAdmin):
#

admin.site.register(UserLogin)