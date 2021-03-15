from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('products/', views.productsList),
    path('products/<int:id>/', views.productById),
    path('products/rating/uid=<int:uid>&pid=<int:pid>/', views.productsRatingById),
    path('products/measurement/pid=<int:pid>', views.productsMeasurementById),
    path('products/measurement/pid=<int:pid>/mid=<str:mid>', views.productsMeasurementById),
    path('products/measurement/pid=<int:pid>/mid=<str:mid>/', views.productsMeasurementById),
    path('products/measurement/pid=<int:pid>/mid=<str:mid>/units=<str:units>', views.productsMeasurementById),
]