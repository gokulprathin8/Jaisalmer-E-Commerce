from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('products/', views.productsList),
    path('products/rating/<int:uid>&<int:pid>', views.productsRatingById),
    path('products/<int:id>', views.productById),
]