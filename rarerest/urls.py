from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rarerestapi.views import register_user, login_user, CategoryView, RareUserView, TagView
from rarerestapi.views.post import PostView
from rarerestapi.views.users import RareUserView

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'categories', CategoryView, 'categories')
router.register(r'posts', PostView, 'posts')
router.register(r'users', RareUserView, 'users')
router.register(r'tags', TagView, 'tags')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
