from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    bar_code = models.CharField(max_length=20)
    net_weight = models.CharField(max_length=10, blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)