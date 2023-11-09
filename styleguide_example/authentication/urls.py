from django.urls import path, include

from .apis import (
    UserSessionLoginApi,
    UserSessionLogoutApi,

    # UserJwtLoginApi,
    # UserJwtLogoutApi,

    UserMeApi,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'session/',
        include(([
            path(
                'login/',
                UserSessionLoginApi.as_view(),
                name='login'
            ),
            path(
                'logout/',
                UserSessionLogoutApi.as_view(),
                name='logout'
            )

        ], "session"))
    ),
    path(
        'jwt/',
        include(([
            path(
                "token/",
                TokenObtainPairView.as_view(),
                name="token_obtain_pair"
            ),
            path(
                "token/refresh/",
                TokenRefreshView.as_view(),
                name="token_refresh"
            )
        ], "jwt"))
    ),
    path(
        'me/',
        UserMeApi.as_view(),
        name='me'
    )
]
