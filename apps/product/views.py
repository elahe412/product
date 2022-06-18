
from traceback import print_tb
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from rest_framework import viewsets

from apps.product.serializers import Listserializer, productSerializer

from apps.product.models import Picture, Product

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializer

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            data._mutable = True
            images = {'images':data.pop('images',None)}
            new_product = self.serializer_class(data= data)
            if new_product.is_valid():
                new_product.save()
                if images['images'] is not None:
                    images_serializer = Listserializer(data =images)
                    images_serializer.is_valid(raise_exception=True)
                    for image in images_serializer.data['images']:
                        Picture.objects.create(image=image,product = new_product.instance)
                product_id = new_product.instance.id
                return JsonResponse({'id':product_id,'success':True},status = HTTP_201_CREATED)
            else:
                return JsonResponse({'error':new_product.errors,'success':False},status=HTTP_400_BAD_REQUEST)
        except Exception as error:
            return JsonResponse({'error':str(error),'success':False},status=HTTP_400_BAD_REQUEST)





