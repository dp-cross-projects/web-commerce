from django.contrib import admin
from .models import UserHistory, UserOrder

# Register models UserHistory and User Order
admin.site.register(UserHistory)
admin.site.register(UserOrder)