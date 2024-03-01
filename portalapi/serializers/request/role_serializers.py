from rest_framework import serializers

from portalapi.models import Role, Scope


class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        fields = ("id", "scope")


class RoleSerializer(serializers.ModelSerializer):
    scopes = ScopeSerializer(many=True)

    class Meta:
        model = Role
        fields = ("scopes",)
        extra_kwargs = {"scopes": {"required": False}}
