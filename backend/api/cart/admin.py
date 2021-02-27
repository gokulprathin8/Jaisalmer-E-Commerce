from django.contrib import admin
from . import models

# product_name = models.CharField(max_length=1024)
# product_price = models.PositiveBigIntegerField()
# product_description = models.TextField()
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)

class ProductRating(admin.TabularInline):
    model = models.ProductRating

class ProductMeasurements(admin.TabularInline):
    model = models.ProductMeasurements

class ProductInline(admin.ModelAdmin):
    inlines = [ProductRating, ProductMeasurements]
    list_display = ('product_name', 'product_price', 'product_description',)

class ProductAdmin(admin.ModelAdmin):
    model = models.Product


admin.site.register(models.Product, ProductInline)