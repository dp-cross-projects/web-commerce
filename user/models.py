from django.db import models
from django.contrib.auth.models import User
from home.models import Product

# Create your models here.
# class UserData(models.Model):
#     user_data = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)

#     def __str__(self):
#         return self.surname + ', ' + self.name

class UserOrder(models.Model):
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    province = models.CharField(max_length=200)
    phone = models.IntegerField()
    total_payment = models.FloatField()

class UserHistory(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    total_amount = models.FloatField()

    def __str__(self):
        return self.user.first_name + ' - ' + self.date + ' - $' + self.total_amount
    
