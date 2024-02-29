from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from portalapi.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "role",
            "is_contact_verified",
            "is_email_verified",
        ]
        read_only_fields = ["id", "is_contact_verified", "is_email_verified"]
        extra_kwargs = {"password": {"write_only": True}}


class CustomTokenPairSerializer(TokenObtainPairSerializer):
    """
    Serializer for custom token pair response.

    This serializer extends TokenObtainPairSerializer to include custom data
    in the token response.

    Attributes:
        user: User data included in the token response.
        role: Role data included in the token response.
        token: Access token included in the token response.
        refresh_token: Refresh token included in the token response.
        has_profile: A flag indicating whether the user has a profile.
    """

    def validate(self, attrs):
        """
        Validate the token attributes.

        Args:
            attrs (dict): The token attributes.

        Returns:
            dict: The validated token response data.
        """
        data = super().validate(attrs)
        user_data = UserSerializer(self.user).data
        response_data = {
            "user": user_data,
            "token": data["access"],
            "refresh_token": data["refresh"],
        }
        return response_data
