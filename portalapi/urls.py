from django.urls import include, path
from rest_framework import routers

from portalapi.views.aiding_views import BloodTypeViewSet
from portalapi.views.auth_views import AuthViewSet
from portalapi.views.profile_views import ProfileViewSet

user_router = routers.DefaultRouter()
user_router.register("auth", AuthViewSet, basename="auth")
user_router.register("profile", ProfileViewSet, basename="profile")
aiding_router = routers.DefaultRouter()
aiding_router.register("type", BloodTypeViewSet, basename="type")

urlpatterns = [
    path("", include(user_router.urls)),
    path("blood/", include(aiding_router.urls)),
]
