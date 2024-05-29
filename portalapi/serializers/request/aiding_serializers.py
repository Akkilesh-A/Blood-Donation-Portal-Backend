from rest_framework import serializers

from portalapi.models import BloodType


class BloodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = "__all__"
