from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_cat = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    descriptions = models.TextField(max_length=500)


