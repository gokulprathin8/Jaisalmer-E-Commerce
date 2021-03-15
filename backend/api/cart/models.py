from django.db import models
from django.contrib.auth.models import User
from django_measurement.models import MeasurementField
from measurement.measures import Volume, Area, Mass, Time, Weight
from multiselectfield import MultiSelectField

RATING_CHOICES = [
    ('ONE', 'ONE'),
    ('TWO', 'TWO'),
    ('THREE', 'THREE'),
    ('FOUR', 'FOUR'),
    ('FIVE', 'FIVE'),
]

PRODUCT_MEASUREMENTS_CHOICES = (
    ('AREA', 'AREA'), ('MASS', 'MASS'), ('WEIGHT', 'WEIGHT'), ('TIME', 'TIME'))


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=1024)
    product_price = models.PositiveBigIntegerField()
    product_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "product"
        ordering = ["-created_at"]


class ProductRating(models.Model):
    user = models.ForeignKey(
        User, related_name="user_id", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="p_id", on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING_CHOICES, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_ratings"
        ordering = ["-created_at"]
        unique_together = ['user', 'product']


class ProductMeasurements(models.Model):
    product_measurements = models.ForeignKey(
        Product, related_name="product_measurements_id", on_delete=models.CASCADE)
    product_volume = MeasurementField(
        measurement=Volume, null=True, blank=True)
    product_area = MeasurementField(measurement=Area, null=True, blank=True)
    product_mass = MeasurementField(measurement=Mass, null=True, blank=True)
    product_weight = MeasurementField(
        measurement=Weight, null=True, blank=True)
    product_time = MeasurementField(measurement=Time, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product_measurements"
