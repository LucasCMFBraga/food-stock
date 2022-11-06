from django.db import models
from stock_api.db_models.product import Product


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    notification_list = models.ManyToManyField(Product, blank=True)