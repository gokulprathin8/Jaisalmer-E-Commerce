from rest_framework import serializers

from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('product_name', 'product_price', 'product_description')
        