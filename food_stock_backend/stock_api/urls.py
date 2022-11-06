from django.urls import include, path
from rest_framework import routers
from stock_api.controllers.user_controller import UserController
from stock_api.controllers.product_controller import ProductController

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('products/', ProductController.as_view(), name='product'),
    path('products/<str:bar_code>', ProductController.as_view(), name='product'),
    path('users/', UserController.as_view(), name='users'),
]