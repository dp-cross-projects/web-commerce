from django.db import models
from home.models import Product
from user.models import UserData
# Create your models here.

class CheckOut(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)