from rest_framework import viewsets

from . import models
from . import seralizers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = seralizers.ProductSerializer