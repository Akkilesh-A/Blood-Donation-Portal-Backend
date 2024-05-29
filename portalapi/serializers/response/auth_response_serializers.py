from rest_framework import serializers

from portalapi.serializers.request.user_serializers import UserSerializer


class AuthResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)
    user_data = UserSerializer()
    access_token = serializers.CharField(max_length=255)
    refresh_token = serializers.CharField(max_length=255)
