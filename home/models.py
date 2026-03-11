from django.db import models

# Category Model
### This class is used for categories in products.
class Category(models.Model):
    name = models.CharField(max_length=200)

    ## Used for identification on Admin Panel
    def __str__(self):
        return self.name

# Product Model
### This class is used for products
## Category => Relation with Category model
## Brand => Text, used to save the brand item
## Model => Text, used to save the model item
## Description => Text, used to save the description 
## Price => Float, used to save the item price
## Tax => Float, used to save the tax value
## Discount => Float, used to save the discount value
## Quantity => Integer, used to save the stock item
## Image => Text, used to save the route to image
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

    ## Used for identification on Admin Panel
    def __str__(self):
        return self.category.name + ' ' + self.brand + ' ' + self.model

