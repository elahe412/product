from django.contrib import admin
from .models import Picture, Product

class PictureAdmin(admin.ModelAdmin):
    fields = ['image','product']

admin.site.register(Picture, PictureAdmin)

class ProductAdmin(admin.ModelAdmin):
    fields=  ['title','price','description']
admin.site.register(Product, ProductAdmin)


