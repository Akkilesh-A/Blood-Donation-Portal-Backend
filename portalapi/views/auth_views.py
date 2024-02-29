from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from portalapi.serializers.request.user_serializers import (
    CustomTokenPairSerializer,
    UserSerializer,
)
from portalapi.serializers.response.auth_response_serializers import (
    LoginResponseSerializer,
)


class AuthViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == "login":
            return CustomTokenPairSerializer
        return UserSerializer

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Logged in Successfully", schema=LoginResponseSerializer()
            )
        }
    )
    @action(methods=["post"], url_path="login", detail=False)
    def login(self, *args, **kwargs):
        serializer = CustomTokenPairSerializer(data=self.request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            response_data = {
                "message": "Logged in Successfully",
                "user_data": user_data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], url_path="register", detail=False)
    def register(self, *args, **kwargs):
        pass
