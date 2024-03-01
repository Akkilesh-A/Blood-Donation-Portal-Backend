from rest_framework import serializers

from portalapi.serializers.request.role_serializers import RoleSerializer
from portalapi.serializers.request.user_serializers import UserSerializer


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    user_data = UserSerializer()
    role_data = RoleSerializer()
    refresh_token = serializers.CharField(max_length=255)
