from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from portalapi.utils.admin_builders import CustomUserAdmin
from portalapi.utils.resources import BloodTypeResource

from .models import BloodType, Profile, User


# Register your models here.
class BloodTypeAdmin(ImportExportModelAdmin):
    resource_class = BloodTypeResource


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(BloodType, BloodTypeAdmin)
