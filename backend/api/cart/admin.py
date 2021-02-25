from django.contrib import admin
from . import models

class ProductRating(admin.TabularInline):
    model = models.ProductRating

class ProductMeasurements(admin.TabularInline):
    model = models.ProductMeasurements

class ProductInline(admin.ModelAdmin):
    inlines = [ProductRating, ProductMeasurements]

admin.site.register(models.Product, ProductInline)