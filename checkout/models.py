from django.db import models
from home.models import Product
from django.contrib.auth.models import User
# Create your models here.

class CheckOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name + ' - ' + self.product.category.name + ' ' + self.product.brand + '' + self.product.model + ' - x' + str(self.quantity)