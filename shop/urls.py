from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProductsViewSet, CartsViewSet, UsersViewSet

router = SimpleRouter()
router.register('products', ProductsViewSet, base_name='products')
router.register('carts', CartsViewSet, base_name='carts')
router.register('users', UsersViewSet, base_name='users')

urlpatterns = router.urls