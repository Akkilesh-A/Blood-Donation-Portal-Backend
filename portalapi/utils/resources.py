from import_export import resources

from portalapi.models import BloodType


class BloodTypeResource(resources.ModelResource):
    class Meta:
        model = BloodType
