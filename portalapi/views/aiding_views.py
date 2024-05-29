from rest_framework import viewsets

from portalapi.models import BloodType
from portalapi.serializers.request.aiding_serializers import BloodTypeSerializer


class BloodTypeViewSet(viewsets.ModelViewSet):
    model = BloodType
    queryset = BloodType.objects.all()
    serializer_class = BloodTypeSerializer
