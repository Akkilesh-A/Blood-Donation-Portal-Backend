from django.contrib import admin

from portalapi.utils.admin_builders import CustomUserAdmin

from .models import BloodType, Profile, User

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(BloodType)
