from rest_framework import serializers
from . import models

class NotificationSeralizer(serializers.ModelSerializer):
    class Meta:
        model = models.Notifications
        fields = ['id', 'notification_title', 'notification_body', 'notification_image']