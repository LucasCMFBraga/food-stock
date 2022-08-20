from rest_framework import viewsets

from stock_api.db_models.user_model import User
from stock_api.serializers.user_serializer import UserSerializer

class UserController(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer