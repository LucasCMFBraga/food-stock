from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    bar_code = models.CharField(max_length=20)
    net_weight = models.CharField(max_length=10)
    expiration_date = models.DateField(blank=True, null=True)