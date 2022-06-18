from rest_framework import serializers 
from apps.product.models import Product
from common.validators import validate_image_file
from product_service.settings import IMAGE_TYPES

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Listserializer(serializers.Serializer):
    images = serializers.ListField(max_length =5,allow_empty =True)

    def validate(self,data):
        for item in data['images']:       
            if validate_image_file(item):
                return data





