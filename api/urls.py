from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView
)
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
    path('logout/', views.logoutuser),
    path('feedback/', views.feedback),
    path('comments/', views.comment),
    path('token/',  TokenObtainPairView.as_view(),  # This will act as login
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('save/', views.save, name='save'),
]
