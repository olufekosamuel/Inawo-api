from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

app_name = "users"

urlpatterns = [
    path('edit/', EditUser, name='edituserinfo'),
    path('info/', GetUserInfo, name='userinfo'),
    path('signup/', Registration, name='signup'),
    path('login/', csrf_exempt(LoginView.as_view()), name="login"),
]