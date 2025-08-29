from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
from .views import RegisterView


# API endpoints for auth — keeping it simple for now
urlpatterns = [
    # custom user registration (might move this to accounts app later)
    path("register/", RegisterView.as_view(), name="register"),

    # login route (JWT pair) — I always forget which one is which
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # refresh endpoint (used by frontend when access token expires)
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # path("logout/", ...)   # might add blacklisting later
]
