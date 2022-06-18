from wsgiref.validate import validator
from rest_framework import serializers 
from apps.product.models import Picture, Product
from common.validators import validate_file_size

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Listserializer(serializers.Serializer):
    images = serializers.ListField(max_length =5,allow_empty =True)
    # images = serializers.ListField(max_length =5,allow_empty =True,child=serializers.ImageField(validator=[validate_file_size]))

    def save_images(self):
        for image in self.data['images']:
            image_object = ImageSerializer(image=image)
            print('HHHHHHHHHHHH')
            print(image.name)


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()





