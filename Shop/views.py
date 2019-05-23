from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .models import Products, Carts
from .serializers import ProductsSerializer, CartsSerializer, UsersSerializer
from .permissions import IsCustomer, IsUser

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsCustomer,)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class CartsViewSet(viewsets.ModelViewSet):
    queryset = Carts.objects.all()
    serializer_class = CartsSerializer
    permission_classes = (IsCustomer,)

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(customer=user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsUser,)