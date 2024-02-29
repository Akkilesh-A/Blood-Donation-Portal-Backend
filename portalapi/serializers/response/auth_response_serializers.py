from rest_framework import serializers

from portalapi.serializers.request.user_serializers import UserSerializer


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    user = UserSerializer()
    expires_in = serializers.IntegerField()
    refresh_token = serializers.CharField(max_length=255)
