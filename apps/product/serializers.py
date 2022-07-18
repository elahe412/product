from rest_framework import serializers 
from django.db import transaction

from apps.product.models import Picture, Product
from common.validators import validate_image_file
from product_service.settings import MAX_IMAGE_NUMBER

class productSerializer(serializers.ModelSerializer):

    images = serializers.ListField(max_length = MAX_IMAGE_NUMBER,allow_empty =True)
    class Meta:
        model = Product
        fields = '__all__'

    def validate_images(self,data):
        for item in data:       
            if validate_image_file(item):
                return data

    
    def to_representation(self, instance):
        result = {}
        result['success'], result['id'] = 'true', instance.id
        return result

    def create(self, validated_data):
        images = validated_data.pop('images', False)
        with transaction.atomic():
            product_obj = super().create(validated_data)
            if images:
                Picture.objects.bulk_create(
                    Picture(
                        product=product_obj,
                        image=picture
                    ) for picture in images
                )
        return product_obj
