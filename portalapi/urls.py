from django.urls import include, path
from rest_framework import routers

from portalapi.views.auth_views import AuthViewSet
from portalapi.views.profile_views import ProfileViewSet

user_router = routers.DefaultRouter()
user_router.register("auth", AuthViewSet, basename="auth")
user_router.register("profile", ProfileViewSet, basename="profile")

urlpatterns = [
    path("", include(user_router.urls)),
]
