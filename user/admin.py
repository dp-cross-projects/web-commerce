from django.contrib import admin
from .models import UserHistory, UserOrder

# Register your models here.
admin.site.register(UserHistory)
admin.site.register(UserOrder)