from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register('notifications', views.NotificationViewSet, basename='notifications')
urlpatterns = [
    path(r"", include(router.urls)),
]
