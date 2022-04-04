from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [
    # path('', views.index),
    # path('login', obtain_auth_token),
    path('signup', views.signup),
    path('logout', views.logoutuser),
    path('feedback', views.feedback),
    path('comment', views.comment),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    # path('save/', views.save, name='save'),
]
