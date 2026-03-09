from django.db import models
from django.contrib.auth.models import User
from home.models import Product

# Create your models here.
class UserData(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField(max_length=5)
    province = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=12)

class UserHistory(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    date = models.DateTimeField()
    product = models.ForeignKey(Product)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    total_payment = models.FloatField()