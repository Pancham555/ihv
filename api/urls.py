from django.urls import path
from api import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('', views.index),
    path('login', obtain_auth_token),
    path('signup', views.signup),
    path('logout', views.logoutuser),
    path('feedback', views.feedback),
    path('comment', views.comment),
    # path('save/', views.save, name='save'),
]
