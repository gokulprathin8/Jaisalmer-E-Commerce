from django_measurement.models import MeasurementField
from measurement.measures import Area
from measurement.measures import Mass
from measurement.measures import Time
from measurement.measures import Volume
from measurement.measures import Weight
from rest_framework import serializers

from . import models


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ("user", "product", "rating")


class ProductAllRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ("product", "rating")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ("product_id", "product_name", "product_price",
                  "product_description")


class ProductMeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductMeasurements
        fields = (
            "product_volume",
            "product_area",
            "product_mass",
            "product_weight",
            "product_time",
            "product_measurements",
        )
