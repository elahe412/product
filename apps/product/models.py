from hashlib import blake2b
from django.db import models

from common.bases.base_model import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=500)
    price  = models.DecimalField(max_digits=6, decimal_places=2)

    
    def __str__(self) :
        return f'{self.title}'

class Picture(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

