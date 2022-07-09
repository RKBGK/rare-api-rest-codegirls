from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rarerestapi.views import register_user, login_user, CategoryView
from rarerestapi.views.post import PostView
from rarerestapi.views.users import UserView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'category', CategoryView, 'category')
router.register(r'posts', PostView, 'post')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
