from django_filters import rest_framework as filters
from . import models

class NotificationsFilter(filters.FilterSet):
    class Meta:
        model = models.Notifications
        # fields = ['notification_title']
        fields = {
            "notification_title": ['icontains', 'iexact'],
            "notification_body": ['icontains', 'iexact'],
            "created_at": ['iexact', 'lte', 'gte'],
            "updated_at": ['iexact', 'lte', 'gte']
        }