from django.db import models
from django.contrib.postgres.fields import ArrayField

from common.validators import validate_file_size

class product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price  = models.PositiveIntegerField()
    images = ArrayField(models.FileField(upload_to='images/',validators=[validate_file_size]),size = 5,null=True,blank=True)

    
    def __str__(self) :
        return f'{self.title}'