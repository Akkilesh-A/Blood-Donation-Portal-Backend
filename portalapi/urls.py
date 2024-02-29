from django.urls import include, path
from rest_framework import routers

from portalapi.views.auth_views import AuthViewSet

user_router = routers.DefaultRouter()
user_router.register("auth", AuthViewSet, basename="auth")

urlpatterns = [
    path("", include(user_router.urls)),
]
