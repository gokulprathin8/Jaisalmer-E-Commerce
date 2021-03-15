from rest_framework import serializers
from . import models

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ('user', 'product', 'rating')


# class ProductSerializer(serializers.ModelSerializer):
#     p_id = ProductRatingSerializer(many=True)

#     class Meta:
#         model = models.Product
#         fields = ('product_id','product_name', 'product_price', 'product_description', 'p_id')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('product_id','product_name', 'product_price', 'product_description')