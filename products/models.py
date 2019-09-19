from django.db import models
#from datetime import datetime
#from django.utils import timezone

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100, default="", null=False, blank=False, unique=True)
    description = models.TextField(default="", null=True, blank=True)
    price = models.DecimalField(max_digits=24, decimal_places=2, null=True, blank=True, default=0.00)
    #sale_price = models.DecimalField(max_digits=24, decimal_places=2, null=True, blank=True)
    #timestamp = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.title)

    def get_price(self):
        return self.price
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=True)
    image = models.ImageField(upload_to='products/static/img/', default='products/static/img/1.jpg')
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.product.title)
