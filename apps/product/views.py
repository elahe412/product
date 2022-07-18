from ast import List
from rest_framework import viewsets

from apps.product.serializers import productSerializer
from apps.product.models import Picture, Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer
