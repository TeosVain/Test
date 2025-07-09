from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from avatar.views import AvatarHandlerViewSet


router = DefaultRouter()
router.register(r'avatars', AvatarHandlerViewSet, basename='avatarhandler')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
