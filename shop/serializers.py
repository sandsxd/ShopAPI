from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Products, Carts

class ProductsSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Products
        fields = ('name', 'sku', 'customer',)

class CartsSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')

    class Meta:
        model = Carts
        fields = ('products', 'customer',)

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}