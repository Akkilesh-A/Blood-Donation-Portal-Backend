from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from portalapi.models import User
from portalapi.serializers.request.profile_serializers import ProfileSerializer
from portalapi.serializers.request.role_serializers import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating or retrieving a user.

    This serializer handles the serialization and deserialization of User instances.
    It includes validation for contact, email, and password fields.

    Attributes:
        id: User ID.
        email: User email address.
        password: User password.
        role: User role.
        contact: User contact information.
        is_contact_verified: Flag indicating whether the contact information is verified.
        is_email_verified: Flag indicating whether the email address is verified.
    """

    role = RoleSerializer(many=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "role",
            "contact",
            "is_contact_verified",
            "is_email_verified",
        ]
        read_only_fields = ["id", "is_contact_verified", "is_email_verified"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_contact(self, contact):
        """
        Validate the contact field.

        Args:
            contact (str): The contact information.

        Raises:
            serializers.ValidationError: If the contact already exists.

        Returns:
            str: The validated contact information.
        """
        if User.objects.filter(contact=contact).exists():
            raise serializers.ValidationError("Contact already exists.")
        return contact

    def validate_email(self, email):
        """
        Validate the email field.

        Args:
            email (str): The email address.

        Raises:
            serializers.ValidationError: If the email already exists.

        Returns:
            str: The validated email address.
        """
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists.")
        return email

    def validate_password(self, password):
        """
        Validate the user's password.

        Args:
            password (str): The password.

        Raises:
            serializers.ValidationError: If the password validation fails.

        Returns:
            str: The hashed password.
        """
        try:
            validate_password(password)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(str(exc))
        password = make_password(password)
        return password


class LoginSerializer(TokenObtainPairSerializer):
    """
    Serializer for custom token pair response.

    This serializer extends TokenObtainPairSerializer to include custom data
    in the token response.

    Attributes:
        user: User data included in the token response.
        token: Access token included in the token response.
        refresh_token: Refresh token included in the token response.
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


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["email", "contact", "password", "confirm_password"]

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = data["email"]
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def validate_contact(self, contact):
        if User.objects.filter(contact=contact).exists():
            raise serializers.ValidationError("User with same contact already exists.")
        return contact

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with same email already exists.")
        return email


class UserSerializerWithProfile(serializers.ModelSerializer):
    """
    Serializer for creating or retrieving a user.

    This serializer handles the serialization and deserialization of User instances.
    It includes validation for contact, email, and password fields.

    Attributes:
        id: User ID.
        email: User email address.
        password: User password.
        role: User role.
        contact: User contact information.
        is_contact_verified: Flag indicating whether the contact information is verified.
        is_email_verified: Flag indicating whether the email address is verified.
    """

    role = RoleSerializer(many=False)
    profile = ProfileSerializer(many=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "role",
            "contact",
            "profile",
            "is_contact_verified",
            "is_email_verified",
        ]
