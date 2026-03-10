from django.db import models
from django.contrib.auth.models import User
from home.models import Product

class UserOrder(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    province = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __str__(self):
        return str(self.date) + self.user.last_name + ', ' + self.user.first_name

class UserHistory(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    total_amount = models.FloatField()

    def __str__(self):
        return self.user_order.user.last_name + ' - ' + self.product.brand + ' - ' + str(self.total_amount)
    
