from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from portalapi.serializers.request.user_serializers import (
    CustomTokenPairSerializer,
    UserOauthSerializerWithToken,
    UserSerializer,
)
from portalapi.serializers.response.auth_response_serializers import (
    LoginResponseSerializer,
)
from portalapi.utils.constants import ResponseMessage


class AuthViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == "login":
            return CustomTokenPairSerializer
        if self.action == "register_oauth":
            return UserOauthSerializerWithToken
        return UserSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description=ResponseMessage.USERLOGGEDINSUCCESSFULLY.value,
                schema=LoginResponseSerializer(),
            )
        }
    )
    @action(methods=["post"], url_path="login", detail=False)
    def login(self, *args, **kwargs):
        serializer = CustomTokenPairSerializer(data=self.request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            response_data = {
                "message": ResponseMessage.USERLOGGEDINSUCCESSFULLY.value,
                "user_data": user_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], url_path="register/oauth", detail=False)
    def register_oauth(self, *args, **kwargs):
        serializer = UserOauthSerializerWithToken(data=self.request.data)
        if serializer.is_valid():
            user, refresh_token = serializer.save()
            user_serializer = UserSerializer(user, many=False)
            response_data = {
                "message": ResponseMessage.USERREGISTEREDSUCCESSFULLY.value,
                "user_data": user_serializer.data,
                "refresh_token": str(refresh_token),
                "access_token": str(refresh_token.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
