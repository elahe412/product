from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price  = models.PositiveIntegerField()

    
    def __str__(self) :
        return f'{self.title}'

class Picture(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

