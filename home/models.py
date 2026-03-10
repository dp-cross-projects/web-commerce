from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    tax = models.FloatField()
    discount = models.FloatField() 
    quantity = models.IntegerField()
    image = models.CharField()

    def __str__(self):
        return self.category.name + ' ' + self.brand + ' ' + self.model

