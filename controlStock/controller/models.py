from django.db import models

# Create your models here.
class Products(models.Model):
    typeProduct = models.CharField(max_length=100)
    nameProduct = models.CharField(max_length=100, default='')
    amountProduct = models.IntegerField(default=0, null=True)
    priceProduct = models.DecimalField(max_digits=10, decimal_places=2, null=True)

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)