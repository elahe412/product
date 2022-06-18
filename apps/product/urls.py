from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.product.views import ProductViewSet
urlpatterns = []
router = DefaultRouter()

router.register('', ProductViewSet, basename='product')
urlpatterns += router.urls
