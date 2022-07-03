from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rarerestapi.views import register_user, login_user


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls)
]
