from django.contrib import admin
from .models import Products, Carts

# Register your models here.
admin.site.register(Products)
admin.site.register(Carts)