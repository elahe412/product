from rest_framework import viewsets
from apps.product.serializers import productSerializer

from models import product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer
