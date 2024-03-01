from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from portalapi.models import User
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
            "password",
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

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data (dict): The validated user data.

        Returns:
            tuple: A tuple containing the created user instance and the associated refresh token.
        """
        user = User.objects.create_user(**validated_data)
        refresh_token = RefreshToken.for_user(user)
        return user, refresh_token

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


class CustomTokenPairSerializer(TokenObtainPairSerializer):
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


class UserOauthSerializerWithToken(UserSerializer):
    """
    Serializer for creating or retrieving a user with OAuth authentication.

    This serializer extends UserSerializer to accommodate OAuth authentication,
    specifically tailored for scenarios where the user's email serves as the username.

    Attributes:
        email: Email field for the user.
    """

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, attrs):
        """
        Validate the user attributes.

        Args:
            attrs (dict): The user attributes.

        Returns:
            dict: The validated user data.
        """
        attrs["username"] = attrs["email"]
        return attrs

    def validate_email(self, email):
        """
        Validate the email field.

        Args:
            email (str): The email address.

        Returns:
            str: The validated email.
        """
        return email

    def create(self, validated_data):
        """
        Create a new user instance.

        Args:
            validated_data (dict): The validated user data.

        Returns:
            tuple: A tuple containing the created user instance and the associated refresh token.
        """
        if User.objects.filter(email=validated_data["email"]).exists():
            user = User.objects.get(email=validated_data["email"])
        else:
            user = User.objects.create_user(**validated_data)
        refresh_token = RefreshToken.for_user(user)
        return user, refresh_token
