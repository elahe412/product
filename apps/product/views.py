
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from apps.product.serializers import Listserializer, productSerializer

from apps.product.models import Picture, Product

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer

    def create(self,request,*args,**kwargs):
        data = request.data

        images = {'images':data.pop('images')}
        print(images,type(images))
        new_product = productSerializer(data= data)
        print(1)
        new_product.is_valid(raise_exception=True)
        new_product.save()
        images_serializer = Listserializer(data =images)
        print(2)
        images_serializer.is_valid(raise_exception=True)
        print(3)
        for image in images_serializer.data['images'] :
            print(4)
            Picture.objects.create(image=image,product = new_product.instance)
        return HttpResponse(status = 201)






@api_view(['POST',])
def list_test(request, *args, **kwargs):
    print(request)
    print('FIIILESSSSSSSSSSSSss')
    
    serializer = Listserializer(data = request.FILES)
    serializer.is_valid(raise_exception=True)
    serializer.save_images()
    # print(serializer.data)
    # print(type(serializer.data['images'][1]))
    
    for image in serializer.data['images'] :
        print(type(image))
        print(image.name)

