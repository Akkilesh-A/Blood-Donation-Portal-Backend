from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from portalapi.serializers.request.user_serializers import UserSerializerWithProfile


class ProfileViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserSerializerWithProfile

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        user = request.user
        user_data = UserSerializerWithProfile(user).data
        return Response(user_data, status.HTTP_200_OK)
