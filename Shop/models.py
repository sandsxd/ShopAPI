from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=15)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Customer: {} | Product: {} | SKU: {}'.format(self.customer.username, self.name, self.sku)

    class Meta:
        verbose_name="product"
        verbose_name_plural="products"

class Carts(models.Model):
    products = ArrayField(models.CharField(max_length=100), default=list)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name="cart"
        verbose_name_plural="carts"