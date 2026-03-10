from django.db import models
from home.models import Product
from django.contrib.auth.models import User

# CheckOut Model
### This class is used for elements in cart.

## User => Relation with Django User Model
## Product => Relation with Home Product Model
## Quantity => Total items from the same product on cart 
class CheckOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    ## Used for identification on Admin Panel
    def __str__(self):
        return self.user.first_name + ' - ' + self.product.category.name + ' ' + self.product.brand + '' + self.product.model + ' - x' + str(self.quantity)