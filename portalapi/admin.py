from django.contrib import admin

from portalapi.utils.admin_builders import CustomUserAdmin

from .models import User

# Register your models here.
admin.site.register(User, CustomUserAdmin)
