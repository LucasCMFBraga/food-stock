from rest_framework import serializers

from stock_api.db_models.user_model import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "notification_list")