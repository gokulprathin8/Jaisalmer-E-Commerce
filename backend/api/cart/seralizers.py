from rest_framework import serializers

from . import models


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ('user', 'product_rating', 'rating')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ('product_id','product_name', 'product_price', 'product_description')