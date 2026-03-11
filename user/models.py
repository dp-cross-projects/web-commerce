from django.db import models
from django.contrib.auth.models import User
from home.models import Product

# UserOrder Model
### This class is used to save purchase order.

## Date => Create a timestamp when created a row
## User => Relation with Django User Model
## Address => Text, used to save address
## Zip Code => Integer, used to save Zip Code
## Province => Text, used to save province name
## Phone => Integer, used to save phone number
## Total Amount => Float, used to save total amount from order

class UserOrder(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    province = models.CharField(max_length=200)
    phone = models.IntegerField()
    total_amount = models.FloatField()

    ## Used for identification on Admin Panel
    def __str__(self):
        return str(self.date) + self.user.last_name + ', ' + self.user.first_name

# UserHistory Model
### This class is used to save items from purchase order.

## User Order => Relation with User Order
## Product => Relation with Home Product Model
## Category => Text, used to copy the category name from Product
## Brand => Text, used to copy the brand name from Product
## Model => Integer, used to copy the model name from Product

class UserHistory(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    
    ## Used for identification on Admin Panel
    def __str__(self):
        return self.user_order.user.last_name + ' - ' + self.product.brand
    
