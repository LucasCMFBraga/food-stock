from dataclasses import field
from rest_framework.serializers import ModelSerializer

from stock_api.db_models.product import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "bar_code", "net_weight", "expiration_date"]
    
    def update(self, instance: Product, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.bar_code = validated_data.get("bar_code", instance.bar_code)
        instance.expiration_date = validated_data.get("expiration_date", instance.expiration_date)
        instance.net_weight = validated_data.get("net_weight", instance.net_weight)
        instance.save()

        return instance