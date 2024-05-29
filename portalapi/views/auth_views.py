from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from portalapi.models import User
from portalapi.serializers.request.user_serializers import (
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)
from portalapi.serializers.response.auth_response_serializers import (
    AuthResponseSerializer,
)
from portalapi.utils.constants import ResponseMessage


class AuthViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        if self.action == "register":
            return RegisterSerializer
        return UserSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description=ResponseMessage.USERLOGGEDINSUCCESSFULLY.value,
                schema=AuthResponseSerializer(),
            )
        }
    )
    @action(methods=["post"], url_path="login", detail=False)
    def login(self, *args, **kwargs):
        serializer = LoginSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_data = serializer.validated_data
        refresh_token, access_token = user_data.pop("refresh_token"), user_data.pop(
            "token"
        )
        response_data = {
            "message": ResponseMessage.USERLOGGEDINSUCCESSFULLY.value,
            "user_data": user_data,
            "access_token": str(access_token),
            "refresh_token": str(refresh_token),
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description=ResponseMessage.USERREGISTEREDSUCCESSFULLY.value,
                schema=AuthResponseSerializer(),
            )
        }
    )
    @action(methods=["POST"], url_path="register", detail=False)
    def register(self, *args, **kwargs):
        serializer = RegisterSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.validated_data.pop("confirm_password")
        user = User.objects.create_user(**serializer.validated_data)
        refresh_token = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        response_data = {
            "message": ResponseMessage.USERREGISTEREDSUCCESSFULLY.value,
            "user_data": user_data,
            "access_token": str(refresh_token.access_token),
            "refresh_token": str(refresh_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
