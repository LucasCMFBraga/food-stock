from django.urls import include, path
from rest_framework import routers
from stock_api.controllers.user_controller import UserController
from stock_api.controllers.product_controller import ProductController

router = routers.DefaultRouter()
router.register(r'user', UserController)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductController.as_view(), name='product'),
    path('products/<str:bar_code>', ProductController.as_view(), name='product'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]