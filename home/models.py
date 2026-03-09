from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField() 
    quantity = models.IntegerField()
    image = models.BinaryField()